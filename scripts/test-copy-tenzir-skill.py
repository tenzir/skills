#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///
"""Tests for copy-tenzir-skill.py against a local stand-in for tenzir.com.

The site serves its docs at /docs/, whose pages link their absolute addresses.
Small sites below their own prefix, such as /flaky/docs/, each exercise one
failure.
"""

from __future__ import annotations

import contextlib
import http.server
import importlib.util
import io
import tempfile
import threading
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "copy_tenzir_skill", Path(__file__).with_name("copy-tenzir-skill.py")
)
assert spec and spec.loader
copy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(copy)
# Retries of server errors need no backoff here.
copy.time.sleep = lambda seconds: None

SKILL_MAP = """---
name: tenzir
description: >-
  Answer questions.
---

# Tenzir Documentation Map

Every link below is relative to <{root}>.
See <{site}/changelog.md> and [integrations]({site}/integrations/splunk.md).

- [Operators](reference/operators.md)
- [Guides](guides.md)
"""

OPERATORS = """# Operators

- [where]({root}reference/operators/where.md)
- [Guides]({root}guides.md#parsing)
- [Platform]({site}/docs/reference/platform.md)
- [Older]({site}/docs/v5.0.0/guides.md)
- [Gone]({root}reference/operators/gone.md)
- [Spec]({root}_downloads/node.yaml)
- [Escape]({root}/tmp/outside.md)

[ref]: {root}guides.md

Inline `[code]({root}guides.md)` stays.

````md
[fenced]({root}guides.md)
```
[still fenced]({root}guides.md)
````
"""

WHERE = "# where\n\nSee [Operators]({root}reference/operators.md#top).\n"
GUIDES = "# Guides\n\nSee [where](reference/operators/where.md).\n"


MINI_MAP = "---\nname: tenzir\n---\n\n- [Guides](guides.md)\n"


def corpus(root: str, site: str) -> dict[str, str]:
    pages = {
        "reference/operators.md": OPERATORS,
        "reference/operators/where.md": WHERE,
        "guides.md": GUIDES,
        # Served, so that only the copy keeps it out of the skill.
        "/tmp/outside.md": "# Outside\n",
    }
    return {path: text.format(root=root, site=site) for path, text in pages.items()}


class Site(http.server.ThreadingHTTPServer):
    request_queue_size = 64
    # A body, an HTTP status, or a redirect target as `("Location", url)`.
    pages: dict[str, str | int | tuple[str, str]]


class Handler(http.server.BaseHTTPRequestHandler):
    server: Site

    def log_message(self, *args: object) -> None:
        pass

    def do_GET(self) -> None:
        body = self.server.pages.get(self.path, 404)
        if isinstance(body, int):
            self.send_error(body)
            return
        if isinstance(body, tuple):
            self.send_response(307)
            self.send_header(*body)
            self.end_headers()
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body.encode())


class CopyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = Site(("127.0.0.1", 0), Handler)
        cls.site = f"http://127.0.0.1:{cls.server.server_port}"
        cls.root = f"{cls.site}/docs/"
        pages: dict[str, str | int | tuple[str, str]] = {
            "/docs/SKILL.md": SKILL_MAP.format(root=cls.root, site=cls.site)
        }
        for path, text in corpus(cls.root, cls.site).items():
            pages["/docs/" + path] = text
        other_origin = f"http://localhost:{cls.server.server_port}"

        def mini(name: str, guides: str, **extra: str | int | tuple[str, str]):
            root = f"/{name}/docs/"
            pages[root + "SKILL.md"] = MINI_MAP
            pages[root + "guides.md"] = guides.format(root=cls.site + root)
            pages.update({root + path: value for path, value in extra.items()})

        # A transitive page fails with a server error.
        mini("flaky", "[Flaky]({root}flaky.md)\n", **{"flaky.md": 503})
        # Transitive pages redirect to another release and another origin.
        mini(
            "redirects",
            "[Version]({root}version.md) [Origin]({root}origin.md)\n",
            **{
                "version.md": ("Location", "/docs/v5.0.0/guides.md"),
                "origin.md": ("Location", f"{other_origin}/redirects/docs/x.md"),
            },
        )
        pages["/docs/v5.0.0/guides.md"] = "# Foreign\n"
        pages["/redirects/docs/x.md"] = "# Foreign\n"
        # A page the map links redirects to another release.
        pages["/required/docs/SKILL.md"] = MINI_MAP
        pages["/required/docs/guides.md"] = ("Location", "/docs/v5.0.0/guides.md")
        # The map itself redirects.
        pages["/moved/docs/SKILL.md"] = ("Location", "/docs/SKILL.md")
        cls.server.pages = pages
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()

    def crawl(self, name: str = "") -> tuple[dict[str, bytes], str, str]:
        """The copied files, the docs root, and the warnings."""
        root = f"{self.site}/{name}/docs/" if name else self.root
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            files = copy.crawl(root)
        return files, root, stderr.getvalue()

    def copy(self) -> dict[str, str]:
        files, root, _ = self.crawl()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "tenzir"
            copy.write(copy.localize(files, root), output)
            self.assertEqual(
                sorted(file.name for file in Path(directory).iterdir()), ["tenzir"]
            )
            return {
                str(file.relative_to(output)): file.read_text()
                for file in output.rglob("*")
                if file.is_file()
            }

    def test_copies_the_pages_the_map_reaches(self) -> None:
        self.assertEqual(
            sorted(self.copy()),
            [
                "SKILL.md",
                "guides.md",
                "reference/operators.md",
                "reference/operators/where.md",
            ],
        )

    def test_rewrites_links_to_copied_pages(self) -> None:
        files = self.copy()
        operators = files["reference/operators.md"]
        self.assertIn("- [where](operators/where.md)", operators)
        self.assertIn("- [Guides](../guides.md#parsing)", operators)
        self.assertIn("[ref]: ../guides.md\n", operators)
        self.assertIn(
            "[Operators](../operators.md#top)", files["reference/operators/where.md"]
        )
        # Relative links stay as the website wrote them.
        self.assertIn("[where](reference/operators/where.md)", files["guides.md"])
        self.assertIn("- [Guides](guides.md)", files["SKILL.md"])

    def test_keeps_links_outside_the_copy_and_in_code(self) -> None:
        site, root = self.site, self.root
        files = self.copy()
        operators = files["reference/operators.md"]
        for kept in [
            f"[Older]({site}/docs/v5.0.0/guides.md)",
            f"[Gone]({root}reference/operators/gone.md)",
            f"[Spec]({root}_downloads/node.yaml)",
            f"`[code]({root}guides.md)`",
            f"[fenced]({root}guides.md)",
            f"[still fenced]({root}guides.md)",
        ]:
            self.assertIn(kept, operators)
        self.assertIn(
            f"[integrations]({site}/integrations/splunk.md)", files["SKILL.md"]
        )
        self.assertIn(f"<{root}>", files["SKILL.md"])

    def test_fails_without_an_agent_map(self) -> None:
        with self.assertRaisesRegex(copy.CopyError, r"no agent map .* \(HTTP 404\)"):
            copy.crawl(f"{self.site}/missing/docs/")

    def test_keeps_paths_below_the_output_directory(self) -> None:
        page = self.root + "guides.md"
        self.assertIsNone(copy.docs_path("/docs//tmp/outside.md", page, self.root))
        files, _, _ = self.crawl()
        self.assertNotIn("/tmp/outside.md", files)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "tenzir"
            for path in ["/tmp/outside.md", "../outside.md", "a/../../outside.md"]:
                with self.assertRaisesRegex(copy.CopyError, "outside"):
                    copy.write({path: b"# Outside\n"}, output)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_fails_on_server_errors_and_warns_on_missing_pages(self) -> None:
        with self.assertRaisesRegex(copy.CopyError, r"flaky\.md: HTTP 503"):
            self.crawl("flaky")
        files, _, warnings = self.crawl()
        self.assertNotIn("reference/operators/gone.md", files)
        self.assertIn("broken link to", warnings)
        self.assertIn("gone.md (HTTP 404)", warnings)

    def test_rejects_redirects_outside_the_docs(self) -> None:
        files, _, warnings = self.crawl("redirects")
        self.assertEqual(sorted(files), ["SKILL.md", "guides.md"])
        self.assertIn("version.md, which redirects to", warnings)
        self.assertIn("origin.md, which redirects to http://localhost:", warnings)
        with self.assertRaisesRegex(copy.CopyError, "outside the docs"):
            self.crawl("required")
        with self.assertRaisesRegex(copy.CopyError, "outside the docs"):
            self.crawl("moved")


if __name__ == "__main__":
    unittest.main()
