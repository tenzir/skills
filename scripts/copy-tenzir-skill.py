#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///
"""Copy the tenzir skill from the agent map that tenzir.com publishes.

Every docs release on the website carries an agent map at
``/docs/v<version>/SKILL.md``: the skill's frontmatter and a condensed map of
the release, whose relative links lead to the release's Markdown twins. This
script downloads the map and every twin of the release it reaches, following
links from page to page, and mirrors them below the output directory.

The twins link each other with absolute URLs, such as
``https://tenzir.com/docs/v7.0.0/reference/operators/where.md``, so the copy
follows absolute links into the release as well. The latest release, as
``/docs/versions.json`` names it, serves its twins at ``/docs/`` and
redirects there from its versioned address, so for it the copy accepts that
address, too. It rejects every other redirect, so no page of another release
or site enters the skill.

The copy rewrites links to the pages it copied into paths relative to the
linking file, keeping their anchors, so the skill navigates offline. It leaves
links in code and links outside the release as they are.
"""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.request
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urldefrag, urljoin

SKILL_MAP = "SKILL.md"
USER_AGENT = "tenzir-skills-sync (+https://github.com/tenzir/skills)"

# Pages of other corpora below a docs root, which the copy never follows.
OTHER_CORPUS = re.compile(r"^(?:v\d+\.\d+\.\d+|unreleased|latest)(?:/|\.md$)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
CODE_SPAN = re.compile(r"(`+).*?\1")
INLINE_LINK = re.compile(r"(\]\(\s*<?)([^)\s>]+)")
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>")
DEFINITION = re.compile(r"^(\s{0,3}\[[^\]]+\]:\s*<?)([^\s>]+)")


class CopyError(Exception):
    pass


def fetch(url: str) -> tuple[str, bytes]:
    """The final URL after redirects and the body of a GET request."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.geturl(), response.read()
        except urllib.error.HTTPError as error:
            if error.code < 500 or attempt == 2:
                raise
        except OSError:
            # Connection failures, such as resets and timeouts.
            if attempt == 2:
                raise
        time.sleep(2**attempt)
    raise AssertionError("unreachable")


def release_roots(base_url: str, release: str) -> list[str]:
    """The addresses of a release's docs: its versioned root and, for the
    latest release, the unversioned `/docs/` where its pages answer."""
    base = base_url.rstrip("/")
    url = f"{base}/docs/versions.json"
    try:
        latest = json.loads(fetch(url)[1])["latest"]
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise CopyError(f"cannot read the latest release from {url}: {error}")
    version = latest if release == "latest" else release.removeprefix("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[\w.]+)?", version):
        raise CopyError(f"not a release version: {version!r}")
    root = f"{base}/docs/v{version}/"
    return [root, f"{base}/docs/"] if version == latest else [root]


def map_links(markdown: str, href_map: Callable[[str], str]) -> str:
    """A Markdown text with its link destinations outside code mapped.

    Inline links and reference definitions get the mapped destination.
    Autolinks are passed to the mapping but keep their destination, because
    an autolink can only hold an absolute URL.
    """
    out: list[str] = []
    fence = None
    for line in markdown.splitlines(keepends=True):
        if match := FENCE.match(line):
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            out.append(line)
            continue
        if fence is not None:
            out.append(line)
            continue
        line = DEFINITION.sub(lambda m: m.group(1) + href_map(m.group(2)), line)
        prose, last = [], 0
        for span in CODE_SPAN.finditer(line):
            prose.append(map_prose(line[last : span.start()], href_map))
            prose.append(span.group(0))
            last = span.end()
        prose.append(map_prose(line[last:], href_map))
        out.append("".join(prose))
    return "".join(out)


def map_prose(text: str, href_map: Callable[[str], str]) -> str:
    for url in AUTOLINK.findall(text):
        href_map(url)
    return INLINE_LINK.sub(lambda m: m.group(1) + href_map(m.group(2)), text)


def links(markdown: str) -> list[str]:
    """The link destinations of a Markdown text outside code."""
    found: list[str] = []

    def record(href: str) -> str:
        found.append(href)
        return href

    map_links(markdown, record)
    return found


def release_path(href: str, page_url: str, roots: list[str]) -> str | None:
    """The path of a link below a release root, if it leads to a twin."""
    url = urldefrag(urljoin(page_url, href)).url.split("?")[0]
    if not url.endswith(".md"):
        return None
    for root in sorted(roots, key=len, reverse=True):
        if not url.startswith(root):
            continue
        path = url[len(root) :]
        if path == SKILL_MAP or OTHER_CORPUS.match(path) or not safe_path(path):
            return None
        return path
    return None


def safe_path(path: str) -> bool:
    """Whether a path stays below the directory it is relative to."""
    parts = path.split("/")
    return not any(
        part in ("", ".", "..") or "\\" in part or "\0" in part or ":" in part
        for part in parts
    )


def crawl(roots: list[str], jobs: int = 8) -> dict[str, bytes]:
    """The agent map of a release and every twin it reaches, by path."""
    root = roots[0]
    map_url = root + SKILL_MAP
    try:
        final, skill_map = fetch(map_url)
    except urllib.error.HTTPError as error:
        raise CopyError(
            f"no agent map at {map_url} (HTTP {error.code}); the website "
            "publishes one per release since tenzir/content#610"
        )
    except OSError as error:
        raise CopyError(f"cannot download {map_url}: {error}")
    if final != map_url:
        raise CopyError(f"{map_url} redirects to {final}, outside the release")
    text = skill_map.decode()
    if not re.match(r"---\r?\nname: tenzir\r?\n", text):
        raise CopyError(f"{map_url} is not the tenzir skill: no `name: tenzir`")

    files = {SKILL_MAP: skill_map}
    # The map's links must resolve; the archive build checks that they do.
    required = {
        path for href in links(text) if (path := release_path(href, map_url, roots))
    }
    if not required:
        raise CopyError(f"{map_url} links no Markdown twins")
    skipped: list[str] = []
    pending = sorted(required)
    seen = set(pending)

    def get(path: str) -> tuple[str, bytes | None]:
        url = root + path
        try:
            final, body = fetch(url)
        except urllib.error.HTTPError as error:
            # Only a page that does not exist is a broken link; any other
            # error would publish an incomplete copy.
            if error.code not in (404, 410) or path in required:
                raise CopyError(f"cannot download {url}: HTTP {error.code}")
            skipped.append(f"a broken link to {url} (HTTP {error.code})")
            return path, None
        except OSError as error:
            raise CopyError(f"cannot download {url}: {error}")
        if final not in (candidate + path for candidate in roots):
            if path in required:
                raise CopyError(f"{url} redirects to {final}, outside the release")
            skipped.append(f"{url}, which redirects to {final} outside the release")
            return path, None
        return path, body

    with ThreadPoolExecutor(max_workers=jobs) as pool:
        while pending:
            batch, pending = pending, []
            for path, body in pool.map(get, batch):
                if body is not None:
                    files[path] = body
            for path in batch:
                if path not in files:
                    continue
                for href in links(files[path].decode()):
                    target = release_path(href, root + path, roots)
                    if target and target not in seen:
                        seen.add(target)
                        pending.append(target)
    for reason in sorted(skipped):
        print(f"warning: skipped {reason}", file=sys.stderr)
    return files


def localize(files: dict[str, bytes], roots: list[str]) -> dict[str, bytes]:
    """The files with absolute links to copied pages made relative."""
    return {
        path: map_links(
            body.decode(), lambda href, path=path: local_href(href, path, files, roots)
        ).encode()
        for path, body in files.items()
    }


def local_href(href: str, path: str, files: dict[str, bytes], roots: list[str]) -> str:
    """A link of a copied page, relative to it if it leads to a copied page."""
    if not re.match(r"^(?:[a-z][a-z\d+.-]*:|/)", href, re.IGNORECASE):
        return href
    target = release_path(href, roots[0] + path, roots)
    if target is None or target not in files:
        return href
    relative = posixpath.relpath(target, posixpath.dirname(path) or ".")
    fragment = urldefrag(href).fragment
    return f"{relative}#{fragment}" if fragment else relative


def write(files: dict[str, bytes], output_dir: Path) -> None:
    """Replace the output directory with the copied files."""
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(dir=output_dir.parent, prefix=".copy-"))
    try:
        for path, body in files.items():
            target = (staging / path).resolve()
            if not safe_path(path) or not target.is_relative_to(staging.resolve()):
                raise CopyError(f"refusing to write {path!r} outside {output_dir}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        if output_dir.exists():
            shutil.rmtree(output_dir)
        os.replace(staging, output_dir)
    finally:
        shutil.rmtree(staging, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--base-url", default="https://tenzir.com", help="website to copy from"
    )
    parser.add_argument(
        "--release",
        default="latest",
        help="release to copy, such as 7.0.0, or `latest` (default)",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("skills/tenzir"), help="skill directory"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="list the files instead of writing them"
    )
    args = parser.parse_args()
    try:
        roots = release_roots(args.base_url, args.release)
        root = roots[0]
        files = localize(crawl(roots), roots)
        if args.dry_run:
            print("\n".join(sorted(files)))
        else:
            write(files, args.output_dir)
    except CopyError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    verb = "Would copy" if args.dry_run else "Copied"
    print(f"{verb} {len(files)} files from {root}{SKILL_MAP}", file=sys.stderr)
    if output := os.environ.get("GITHUB_OUTPUT"):
        with open(output, "a") as file:
            print(f"source={root}{SKILL_MAP}", file=file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
