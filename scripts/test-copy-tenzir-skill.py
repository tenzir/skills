#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///
"""Tests for copy-tenzir-skill.py against a local stand-in for tenzir.com.

The site serves a preview at /docs/v7.0.0/ whose pages link their versioned
addresses, and a latest release whose map answers at /docs/v6.0.0/ while its
pages redirect to /docs/ and link the unversioned addresses.
"""

from __future__ import annotations

import http.server
import importlib.util
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


def corpus(root: str, site: str) -> dict[str, str]:
    pages = {
        "reference/operators.md": OPERATORS,
        "reference/operators/where.md": WHERE,
        "guides.md": GUIDES,
    }
    return {path: text.format(root=root, site=site) for path, text in pages.items()}


class Site(http.server.ThreadingHTTPServer):
    request_queue_size = 64
    pages: dict[str, str]


class Handler(http.server.BaseHTTPRequestHandler):
    server: Site

    def log_message(self, *args: object) -> None:
        pass

    def do_GET(self) -> None:
        prefix = "/docs/v6.0.0/"
        if self.path.startswith(prefix) and not self.path.endswith("SKILL.md"):
            self.send_response(307)
            self.send_header("Location", "/docs/" + self.path[len(prefix) :])
            self.end_headers()
            return
        body = self.server.pages.get(self.path)
        if body is None:
            self.send_error(404)
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body.encode())


class CopyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = Site(("127.0.0.1", 0), Handler)
        cls.site = f"http://127.0.0.1:{cls.server.server_port}"
        pages = {"/docs/versions.json": '{"latest": "6.0.0"}'}
        for version, page_root in [("7.0.0", "/docs/v7.0.0/"), ("6.0.0", "/docs/")]:
            map_root = f"{cls.site}/docs/v{version}/"
            pages[f"/docs/v{version}/SKILL.md"] = SKILL_MAP.format(
                root=map_root, site=cls.site
            )
            for path, text in corpus(cls.site + page_root, cls.site).items():
                pages[page_root + path] = text
        cls.server.pages = pages
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()

    def copy(self, release: str) -> dict[str, str]:
        root = copy.release_root(self.site, release)
        files, roots = copy.crawl(root)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "tenzir"
            copy.write(copy.localize(files, roots), output)
            return {
                str(file.relative_to(output)): file.read_text()
                for file in output.rglob("*")
                if file.is_file()
            }

    def test_copies_the_pages_the_map_reaches(self) -> None:
        for release in ["7.0.0", "latest"]:
            with self.subTest(release=release):
                self.assertEqual(
                    sorted(self.copy(release)),
                    [
                        "SKILL.md",
                        "guides.md",
                        "reference/operators.md",
                        "reference/operators/where.md",
                    ],
                )

    def test_rewrites_links_to_copied_pages(self) -> None:
        for release in ["7.0.0", "latest"]:
            with self.subTest(release=release):
                files = self.copy(release)
                operators = files["reference/operators.md"]
                self.assertIn("- [where](operators/where.md)", operators)
                self.assertIn("- [Guides](../guides.md#parsing)", operators)
                self.assertIn("[ref]: ../guides.md\n", operators)
                self.assertIn(
                    "[Operators](../operators.md#top)",
                    files["reference/operators/where.md"],
                )
                # Relative links stay as the website wrote them.
                self.assertIn(
                    "[where](reference/operators/where.md)", files["guides.md"]
                )
                self.assertIn("- [Guides](guides.md)", files["SKILL.md"])

    def test_keeps_links_outside_the_copy_and_in_code(self) -> None:
        site = self.site
        files = self.copy("7.0.0")
        operators = files["reference/operators.md"]
        root = f"{site}/docs/v7.0.0/"
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
            copy.crawl(f"{self.site}/docs/v1.0.0/")


if __name__ == "__main__":
    unittest.main()
