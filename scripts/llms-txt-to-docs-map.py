#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///
"""Convert the website's llms.txt into the docs-map manifest.

The tenzir.com llms.txt indexes the whole site as flat link lists under
``## Docs``, ``## Integrations``, etc. The skill generator
(generate-tenzir-docs-skill.py) instead expects the heading-tree manifest the
retired docs.tenzir.com served as sitemap.md: ``## Guides`` sections with
``### <group>`` subsections, ``#### [Page](url)`` entries carrying
descriptions and outline bullets, and ``##### [child]`` entries for catalog
items (operators, functions, API endpoints). This script bridges the two so
the generator stays unchanged.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field

H2_RE = re.compile(r"^## (.+)$")
H3_RE = re.compile(r"^### (.+)$")
BULLET_RE = re.compile(r"^- \[([^\]]+)\]\((\S+?\.md)\)(?::\s*(.*))?$")
OUTLINE_RE = re.compile(r"^(  +)- (.*)$")

DOCS_SECTIONS = ("Guides", "Tutorials", "Explanations", "Reference")


@dataclass(slots=True)
class Page:
    title: str
    url: str
    description: str
    outline: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Subsection:
    label: str
    pages: list[Page] = field(default_factory=list)


def parse_llms_txt(text: str) -> tuple[dict[str, Page], dict[str, list[Subsection]], list[Page]]:
    """Return (section landing pages, docs subsections per section, integrations)."""
    landings: dict[str, Page] = {}
    docs: dict[str, list[Subsection]] = {name: [] for name in DOCS_SECTIONS}
    integrations: list[Page] = []

    section: str | None = None
    subsection: Subsection | None = None
    docs_section: str | None = None
    current: Page | None = None

    for line in text.splitlines():
        match = H2_RE.match(line)
        if match:
            section = match.group(1).strip()
            subsection = None
            docs_section = None
            current = None
            continue

        match = H3_RE.match(line)
        if match:
            label = match.group(1).strip()
            current = None
            if section == "Docs" and ": " in label:
                category, group = label.split(": ", 1)
                if category in docs:
                    docs_section = category
                    subsection = Subsection(label=group)
                    docs[category].append(subsection)
                    continue
            docs_section = None
            subsection = None
            continue

        match = BULLET_RE.match(line)
        if match:
            title, url, description = match.groups()
            current = Page(title=title, url=url, description=description or "")
            if section == "Docs" and subsection is None:
                # Preamble bullets: the docs landing page and one landing
                # page per category. Capture the latter as section links.
                for name in DOCS_SECTIONS:
                    if url.endswith(f"/docs/{name.lower()}.md"):
                        landings[name] = current
            elif section == "Docs" and docs_section and subsection is not None:
                subsection.pages.append(current)
            elif section == "Integrations" and "/integrations/" in url:
                integrations.append(current)
            continue

        match = OUTLINE_RE.match(line)
        if match and current is not None:
            indent, item = match.groups()
            prefix = "  " if len(indent) > 2 else ""
            current.outline.append(f"{prefix}- {item}")

    return landings, docs, integrations


def format_page(page: Page, level: int) -> list[str]:
    lines = [f"{'#' * level} [{page.title}]({page.url})", ""]
    if page.description:
        lines.extend([page.description, ""])
    if page.outline:
        lines.extend([*page.outline, ""])
    return lines


def format_subsection(subsection: Subsection) -> list[str]:
    lines = [f"### {subsection.label}", ""]
    # A page nested below an earlier page of the same subsection is a catalog
    # item (operator, function, API endpoint): render it as a compact child
    # entry, like the old sitemap did.
    roots: list[str] = []
    for page in subsection.pages:
        stem = page.url.removesuffix(".md")
        if any(stem.startswith(f"{root}/") for root in roots):
            lines.extend([f"##### [{page.title}]({page.url})", ""])
            continue
        roots.append(stem)
        lines.extend(format_page(page, 4))
    return lines


def convert(text: str) -> str:
    landings, docs, integrations = parse_llms_txt(text)

    lines: list[str] = ["# Tenzir Documentation Map", ""]

    # Carry over the site tagline from the llms.txt header.
    for line in text.splitlines():
        if H2_RE.match(line):
            break
        if line.startswith("> "):
            lines.extend([line, ""])
            break

    for name in DOCS_SECTIONS:
        subsections = docs[name]
        if not subsections:
            continue
        landing = landings.get(name)
        heading = f"## [{name}]({landing.url})" if landing else f"## {name}"
        lines.extend([heading, ""])
        if landing and landing.description:
            lines.extend([landing.description, ""])
        for subsection in subsections:
            lines.extend(format_subsection(subsection))

    if integrations:
        lines.extend(["## Integrations", ""])
        for page in integrations:
            lines.extend(format_page(page, 4))

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to llms.txt")
    parser.add_argument("output", help="Path to write the docs-map manifest")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as handle:
        text = handle.read()
    manifest = convert(text)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(manifest)
    pages = manifest.count("\n#### ") + manifest.count("\n##### ")
    print(f"Wrote {args.output}: {pages} pages", file=sys.stderr)


if __name__ == "__main__":
    main()
