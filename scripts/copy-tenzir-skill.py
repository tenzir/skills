#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///
"""Copy the tenzir skill from the agent map that tenzir.com publishes.

Every docs release on the website carries an agent map at
``/docs/v<version>/SKILL.md``: the skill's frontmatter and a condensed map of
the release, whose relative links lead to the release's Markdown twins. This
script downloads the map and every twin of the release it reaches, following
links from page to page, and mirrors them below the output directory. It
copies every file byte for byte, so links outside the release stay absolute.

The twins link each other with absolute URLs, such as
``https://tenzir.com/docs/v7.0.0/reference/operators/where.md``, so the copy
follows absolute links into the release as well. The latest release serves
its twins at ``/docs/`` and redirects there from its versioned address; the
copy learns that address from the redirect and follows links to it, too.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urldefrag, urljoin

SKILL_MAP = "SKILL.md"
USER_AGENT = "tenzir-skills-sync (+https://github.com/tenzir/skills)"

# Pages of other corpora below a docs root, which the copy never follows.
OTHER_CORPUS = re.compile(r"^(?:v\d+\.\d+\.\d+|unreleased|latest)(?:/|\.md$)")
FENCE = re.compile(r"^\s*(```|~~~)")
CODE_SPAN = re.compile(r"(`+).*?\1")
INLINE_LINK = re.compile(r"\]\(\s*<?([^)\s>]+)")
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>")
DEFINITION = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s|$)")


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


def release_root(base_url: str, release: str) -> str:
    """The address of a release's docs, resolving `latest` on the website."""
    base = base_url.rstrip("/")
    if release == "latest":
        url = f"{base}/docs/versions.json"
        try:
            release = json.loads(fetch(url)[1])["latest"]
        except (OSError, KeyError, ValueError) as error:
            raise CopyError(f"cannot read the latest release from {url}: {error}")
    return f"{base}/docs/v{release.removeprefix('v')}/"


def links(markdown: str) -> list[str]:
    """The link destinations of a Markdown text outside code."""
    found: list[str] = []
    fence = None
    for line in markdown.splitlines():
        if match := FENCE.match(line):
            if fence is None:
                fence = match.group(1)
            elif match.group(1) == fence:
                fence = None
            continue
        if fence is not None:
            continue
        prose = CODE_SPAN.sub("", line)
        found += INLINE_LINK.findall(prose)
        found += AUTOLINK.findall(prose)
        if match := DEFINITION.match(prose):
            found.append(match.group(1))
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
        parts = path.split("/")
        if path == SKILL_MAP or OTHER_CORPUS.match(path) or ".." in parts:
            return None
        return path
    return None


def crawl(root: str, jobs: int = 8) -> dict[str, bytes]:
    """The agent map of a release and every twin it reaches, by path."""
    map_url = root + SKILL_MAP
    try:
        _, skill_map = fetch(map_url)
    except urllib.error.HTTPError as error:
        raise CopyError(
            f"no agent map at {map_url} (HTTP {error.code}); the website "
            "publishes one per release since tenzir/content#610"
        )
    except OSError as error:
        raise CopyError(f"cannot download {map_url}: {error}")
    text = skill_map.decode()
    if not re.match(r"---\r?\nname: tenzir\r?\n", text):
        raise CopyError(f"{map_url} is not the tenzir skill: no `name: tenzir`")

    roots = [root]
    files = {SKILL_MAP: skill_map}
    # The map's links must resolve; the archive build checks that they do.
    required = {
        path for href in links(text) if (path := release_path(href, map_url, roots))
    }
    if not required:
        raise CopyError(f"{map_url} links no Markdown twins")
    missing: list[str] = []
    pending = sorted(required)
    seen = set(pending)

    def get(path: str) -> tuple[str, str | None, bytes | None]:
        try:
            final, body = fetch(root + path)
            return path, final, body
        except urllib.error.HTTPError as error:
            if path in required:
                raise CopyError(f"{root + path} is missing (HTTP {error.code})")
            return path, None, None
        except OSError as error:
            raise CopyError(f"cannot download {root + path}: {error}")

    with ThreadPoolExecutor(max_workers=jobs) as pool:
        while pending:
            batch, pending = pending, []
            for path, final, body in pool.map(get, batch):
                if body is None:
                    missing.append(path)
                    continue
                files[path] = body
                # A redirect reveals another address of the release.
                if final and final != root + path and final.endswith("/" + path):
                    alias = final[: -len(path)]
                    if alias not in roots:
                        roots.append(alias)
            for path in batch:
                if path not in files:
                    continue
                for href in links(files[path].decode()):
                    target = release_path(href, root + path, roots)
                    if target and target not in seen:
                        seen.add(target)
                        pending.append(target)
    for path in sorted(missing):
        print(f"warning: skipped a broken link to {root + path}", file=sys.stderr)
    return files


def write(files: dict[str, bytes], output_dir: Path) -> None:
    """Replace the output directory with the copied files."""
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(dir=output_dir.parent, prefix=".copy-"))
    try:
        for path, body in files.items():
            target = staging / path
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
        root = release_root(args.base_url, args.release)
        files = crawl(root)
    except CopyError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    if args.dry_run:
        print("\n".join(sorted(files)))
    else:
        write(files, args.output_dir)
    verb = "Would copy" if args.dry_run else "Copied"
    print(f"{verb} {len(files)} files from {root}{SKILL_MAP}", file=sys.stderr)
    if output := os.environ.get("GITHUB_OUTPUT"):
        with open(output, "a") as file:
            print(f"source={root}{SKILL_MAP}", file=file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
