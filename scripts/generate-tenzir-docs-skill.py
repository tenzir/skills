#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "markdown-it-py>=3.0.0",
# ]
# ///

from __future__ import annotations

import argparse
import posixpath
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from markdown_it import MarkdownIt


DOCS_URL_PREFIX = re.compile(r"^https?://docs\.tenzir\.com")
EXCLUDED_SOURCE_PATHS = frozenset({
    "changelog.md",
    "reference/ocsf.md",
})
EXCLUDED_SOURCE_PREFIXES = (
    "changelog/",
    "reference/ocsf/",
)
SECTION_MAX_LEVEL = {
    "Guides": 5,
    "Tutorials": 4,
    "Explanations": 4,
    "Integrations": 5,
    "Reference": 4,
}
# In SKILL.md, strip description content from nodes at or above this heading
# level.  Keeps the heading link for navigation but removes the paragraph
# beneath it, keeping the skill file compact.
SKILL_CONTENT_THRESHOLD = 5
MARKDOWN = MarkdownIt()
LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
HEADING_LINK_RE = re.compile(r"^#{1,6}\s+\[([^\]]+)\]\(([^)]+)\)")
HEADING_TEXT_RE = re.compile(r"^#{1,6}\s+(.+)$")
MARKDOWN_ESCAPE_RE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|>])")
REFERENCE_INDEX_PAGES = (
    ("reference/operators.md", "Operator Index"),
    ("reference/functions.md", "Function Index"),
)
SPECIAL_REFERENCE_INDEX_PAGES = frozenset(relative_path for relative_path, _ in REFERENCE_INDEX_PAGES)
SYNTHETIC_REFERENCE_INDEX_DIRS = frozenset({
    "reference/node",
    "reference/platform",
})
# Operator and function indexes are extracted to standalone files instead of
# being inlined into SKILL.md.  Maps source page → (output path, title).
EXTRACTED_INDEX_FILES = {
    source_path: (f"reference/{Path(source_path).stem}-index.md", title)
    for source_path, title in REFERENCE_INDEX_PAGES
}


@dataclass(slots=True)
class Node:
    heading: str | None
    level: int
    content_lines: list[str] = field(default_factory=list)
    children: list["Node"] = field(default_factory=list)
    preserve_bullets: bool = False


def is_changelog_source_path(source_path: str) -> bool:
    normalized = posixpath.normpath(source_path.lstrip("/"))
    if normalized in ("", "."):
        return False
    return normalized in EXCLUDED_SOURCE_PATHS or any(
        normalized.startswith(prefix) for prefix in EXCLUDED_SOURCE_PREFIXES
    )


def is_excluded_source_path(source_path: str) -> bool:
    return is_changelog_source_path(source_path)


def extract_heading_text(line: str) -> str | None:
    match = HEADING_LINK_RE.match(line)
    if match:
        return match.group(1)
    match = HEADING_TEXT_RE.match(line)
    if match:
        return match.group(1)
    return None


def extract_heading_href(line: str) -> str | None:
    match = HEADING_LINK_RE.match(line)
    return match.group(2) if match else None


def unescape_markdown_text(text: str) -> str:
    return MARKDOWN_ESCAPE_RE.sub(r"\1", text)


def normalize_docs_href(href: str | None) -> str | None:
    if href is None:
        return None
    return DOCS_URL_PREFIX.sub("", href)


def to_source_markdown_path(href: str | None) -> str | None:
    if not href:
        return None
    normalized = normalize_docs_href(href)
    if normalized is None or not normalized.startswith("/"):
        return None
    path_part = normalized[1:].split("#", 1)[0].split("?", 1)[0]
    return path_part if path_part.endswith(".md") else None


def get_node_source_path(node: Node) -> str | None:
    return to_source_markdown_path(extract_heading_href(node.heading or ""))


def build_available_source_paths(source_paths: list[str]) -> set[str]:
    return {
        source_path
        for source_path in source_paths
        if source_path != "sitemap.md" and not is_excluded_source_path(source_path)
    }


def is_bullet_line(line: str) -> bool:
    return line.startswith("- ") or line.startswith("  - ")


def trim_blank_lines(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def has_meaningful_content(lines: list[str]) -> bool:
    return any(line.strip() and not is_bullet_line(line) for line in lines)


def parse_heading_tree(markdown: str) -> Node:
    lines = markdown.splitlines()
    root = Node(heading=None, level=0)
    heading_entries: list[tuple[int, str, int, int]] = []

    for token in MARKDOWN.parse(markdown):
        if token.type != "heading_open" or not token.tag.startswith("h") or token.map is None:
            continue
        level = int(token.tag[1:])
        start_line, end_line = token.map
        heading_entries.append((level, lines[start_line], start_line, end_line))

    if not heading_entries:
        root.content_lines = lines
        return root

    root.content_lines = lines[: heading_entries[0][2]]
    stack = [root]
    nodes_in_order: list[Node] = []

    for level, heading_line, _start_line, _end_line in heading_entries:
        while stack[-1].level >= level:
            stack.pop()
        node = Node(heading=heading_line, level=level)
        stack[-1].children.append(node)
        stack.append(node)
        nodes_in_order.append(node)

    for index, node in enumerate(nodes_in_order):
        _level, _heading_line, _start_line, end_line = heading_entries[index]
        next_start = heading_entries[index + 1][2] if index + 1 < len(heading_entries) else len(lines)
        node.content_lines = lines[end_line:next_start]

    return root


def filter_node(node: Node, *, max_depth: int) -> Node | None:
    if node.level > max_depth:
        return None
    source_path = get_node_source_path(node)
    if source_path and is_excluded_source_path(source_path):
        return None

    children = [
        child
        for child in (filter_node(candidate, max_depth=max_depth) for candidate in node.children)
        if child is not None
    ]
    if not children and not has_meaningful_content(node.content_lines) and not source_path:
        return None

    return Node(
        heading=node.heading,
        level=node.level,
        content_lines=list(node.content_lines),
        children=children,
        preserve_bullets=node.preserve_bullets,
    )


def resolve_local_markdown_path(pathname: str, available_source_paths: set[str]) -> str | None:
    candidate = pathname.lstrip("/")
    if candidate in available_source_paths:
        return candidate
    if not candidate.endswith(".md"):
        candidate = f"{candidate}.md"
        if candidate in available_source_paths:
            return candidate
    return None


def rewrite_link_destination(
    href: str,
    from_path: str,
    available_source_paths: set[str],
) -> str | None:
    if not href or href.startswith(("#", "mailto:", "tel:")):
        return href

    normalized = normalize_docs_href(href)
    if normalized is None or not normalized.startswith("/"):
        return href

    hash_index = normalized.find("#")
    query_index = normalized.find("?")
    suffix_candidates = [index for index in (hash_index, query_index) if index > -1]
    suffix_index = min(suffix_candidates) if suffix_candidates else len(normalized)

    pathname = normalized[:suffix_index]
    suffix = normalized[suffix_index:]
    source_path = pathname[1:]
    if source_path.endswith(".md") and is_excluded_source_path(source_path):
        return None

    local_source_path = resolve_local_markdown_path(pathname, available_source_paths)
    if local_source_path is None:
        return f"https://docs.tenzir.com{normalized}"

    from_dir = posixpath.dirname(from_path)
    if from_dir == ".":
        from_dir = ""
    relative = posixpath.relpath(local_source_path, from_dir or ".")
    if relative == ".":
        relative = local_source_path
    return f"{relative}{suffix}"


def rewrite_content(text: str, from_path: str, available_source_paths: set[str]) -> str:
    text = re.sub(r"^> Documentation index:.*\n?", "", text, flags=re.MULTILINE)

    def replace(match: re.Match[str]) -> str:
        bang, label, href = match.groups()
        rewritten_href = rewrite_link_destination(href, from_path, available_source_paths)
        if rewritten_href is None:
            return f"![{label}]" if bang else label
        return f"{bang}[{label}]({rewritten_href})"

    return LINK_RE.sub(replace, text)


def render_node(
    node: Node,
    *,
    level_offset: int = 0,
    from_path: str = "SKILL.md",
    available_source_paths: set[str],
) -> str:
    lines: list[str] = []

    if node.heading:
        level = max(1, min(6, node.level + level_offset))
        heading_text = rewrite_content(node.heading, from_path, available_source_paths)
        heading_text = re.sub(r"^#{1,6}", "#" * level, heading_text)
        lines.extend([heading_text, ""])

    source_lines = (
        node.content_lines
        if node.preserve_bullets
        else [line for line in node.content_lines if not is_bullet_line(line)]
    )
    content_lines = trim_blank_lines(
        [rewrite_content(line, from_path, available_source_paths) for line in source_lines]
    )
    if content_lines:
        lines.extend([*content_lines, ""])

    for child in node.children:
        rendered = render_node(
            child,
            level_offset=level_offset,
            from_path=from_path,
            available_source_paths=available_source_paths,
        )
        if rendered:
            lines.append(rendered)

    return "\n".join(lines)


def strip_deep_content(node: Node, *, threshold: int) -> None:
    """Remove content_lines from nodes at or above the threshold level.

    Keeps heading links for navigation but removes description paragraphs,
    reducing SKILL.md size while preserving the navigable structure.
    """
    if node.level >= threshold:
        node.content_lines = []
    for child in node.children:
        strip_deep_content(child, threshold=threshold)


def _extract_page_title(markdown: str) -> str:
    """Extract the h1 title from a markdown page."""
    for node in parse_heading_tree(markdown).children:
        if node.level == 1:
            text = extract_heading_text(node.heading or "")
            if text:
                return unescape_markdown_text(text)
    return ""


def create_navigation_node() -> Node:
    """Create the navigation routing section for SKILL.md."""
    return Node(
        heading="## How to use this skill",
        level=2,
        content_lines=[
            "",
            "Navigate the documentation based on the type of question:",
            "",
            "| Question type | Where to look |",
            "|---|---|",
            "| \"How do I…\" tasks | [Guides](guides.md) — step-by-step instructions organized by task |",
            "| Operator or function syntax | [Operator Index](reference/operators-index.md) or [Function Index](reference/functions-index.md), then the specific page |",
            "| Integration setup (Splunk, Kafka, S3…) | [Integrations](integrations.md) — per-product setup and pipeline examples |",
            "| Concepts (nodes, pipelines, deployment) | [Explanations](explanations.md) — architecture and design |",
            "| Learning from scratch | [Tutorials](tutorials.md) — guided lessons |",
            "| TQL language rules | [Language](explanations/language.md), [Expressions](reference/expressions.md), [Statements](reference/statements.md) |",
            "",
            "Always read the relevant page before answering. Prefer TQL examples from the",
            "documentation over inventing syntax.",
        ],
    )


def create_examples_node() -> Node:
    """Create the answer-pattern examples section for SKILL.md."""
    return Node(
        heading="## Answer patterns",
        level=2,
        content_lines=[
            "",
            "**Operator syntax question** — *\"How does `where` work?\"*",
            "→ Read [where](reference/operators/where.md), explain the syntax, show the doc's TQL examples.",
            "",
            "**Integration question** — *\"How do I send data to Splunk?\"*",
            "→ Read [Splunk](integrations/splunk.md), provide the pipeline example from the page.",
            "",
            "**Task question** — *\"How do I parse syslog?\"*",
            "→ Read [Parse delimited text](guides/parsing/parse-delimited-text.md) and",
            "[read_syslog](reference/operators/read_syslog.md). Combine the guide's approach",
            "with the operator reference.",
        ],
    )


def generate_extracted_index(
    input_dir: Path,
    source_relative_path: str,
    title: str,
    output_relative_path: str,
    available_source_paths: set[str],
) -> str | None:
    """Generate a standalone categorized index file for operators or functions."""
    source_file = input_dir / source_relative_path
    if not source_file.is_file():
        return None

    page_root = parse_heading_tree(source_file.read_text(encoding="utf-8"))
    title_node = next((c for c in page_root.children if c.level == 1), None)
    if title_node is None:
        return None

    indexed_paths: set[str] = set()
    lines: list[str] = [f"# {title}", ""]

    for category in title_node.children:
        cat_name = extract_heading_text(category.heading or "")
        if not cat_name:
            continue
        cat_links: list[str] = []
        for item in category.children:
            label = extract_heading_text(item.heading or "")
            href = extract_heading_href(item.heading or "")
            if not label or not href:
                continue
            rewritten = rewrite_link_destination(href, output_relative_path, available_source_paths)
            if rewritten is None:
                continue
            source_path = to_source_markdown_path(href)
            if source_path:
                indexed_paths.add(source_path)
            cat_links.append(f"- [{unescape_markdown_text(label)}]({rewritten})")
        if cat_links:
            lines.extend([f"## {cat_name}", "", *cat_links, ""])

    # Find additional pages not covered by the categorized index.
    parent_dir = posixpath.dirname(source_relative_path)
    additional = sorted(
        sp
        for sp in available_source_paths
        if sp.startswith(f"{parent_dir}/")
        and sp != source_relative_path
        and sp not in indexed_paths
    )
    if additional:
        add_links: list[str] = []
        for ap in additional:
            ap_md = (input_dir / ap).read_text(encoding="utf-8")
            ap_title = _extract_page_title(ap_md) or Path(ap).stem.replace("-", " ").title()
            rel = posixpath.relpath(ap, posixpath.dirname(output_relative_path))
            add_links.append(f"- [{ap_title}]({rel})")
        if add_links:
            lines.extend(["## Additional Pages", "", *add_links, ""])

    return "\n".join(lines) if len(lines) > 2 else None


def build_compact_index_node(
    page_markdown: str,
    *,
    index_heading: str,
    index_level: int,
    category_level: int,
    available_source_paths: set[str],
) -> tuple[Node | None, set[str]]:
    page_root = parse_heading_tree(page_markdown)
    title_node = next((child for child in page_root.children if child.level == 1), None)
    if title_node is None:
        return None, set()

    category_nodes: list[Node] = []
    linked_source_paths: set[str] = set()
    for category in title_node.children:
        category_name = extract_heading_text(category.heading or "")
        if not category_name:
            continue
        links: list[str] = []
        for item in category.children:
            label = extract_heading_text(item.heading or "")
            href = extract_heading_href(item.heading or "")
            if (
                not label
                or not href
                or rewrite_link_destination(href, "SKILL.md", available_source_paths) is None
            ):
                continue
            source_path = to_source_markdown_path(href)
            if source_path is not None:
                linked_source_paths.add(source_path)
            label = unescape_markdown_text(label)
            links.append(f"[{label}]({href})")
        if not links:
            continue
        category_nodes.append(
            Node(
                heading=f"{'#' * category_level} {category_name}",
                level=category_level,
                content_lines=[f"- {link}" for link in links],
                preserve_bullets=True,
            )
        )

    if not category_nodes:
        return None, linked_source_paths

    return (
        Node(
            heading=f"{'#' * index_level} {index_heading}",
            level=index_level,
            children=category_nodes,
        ),
        linked_source_paths,
    )


def build_reference_index_nodes(
    input_dir: Path,
    reference_level: int,
    available_source_paths: set[str],
    *,
    skip_compact_indexes: bool = False,
) -> list[Node]:
    index_nodes: list[Node] = []
    index_level = min(6, reference_level + 2)
    category_level = min(6, index_level + 1)
    compact_index_nodes_by_parent: dict[str, Node] = {}
    compact_index_paths_by_parent: dict[str, set[str]] = {}
    for relative_path, index_heading in REFERENCE_INDEX_PAGES:
        source_file = input_dir / relative_path
        if not source_file.is_file():
            continue
        node, indexed_paths = build_compact_index_node(
            source_file.read_text(encoding="utf-8"),
            index_heading=index_heading,
            index_level=index_level,
            category_level=category_level,
            available_source_paths=available_source_paths,
        )
        compact_index_paths_by_parent[relative_path] = indexed_paths
        if node is not None:
            compact_index_nodes_by_parent[relative_path] = node
            if not skip_compact_indexes:
                index_nodes.append(node)

    flat_index_level = min(6, reference_level + 2)
    flat_child_paths_by_parent: dict[str, list[str]] = {}
    for source_path in sorted(available_source_paths):
        if not source_path.startswith("reference/") or source_path.count("/") != 2:
            continue
        parent_dir = posixpath.dirname(source_path)
        parent_path = f"{posixpath.dirname(source_path)}.md"
        if parent_path in available_source_paths or parent_path in SPECIAL_REFERENCE_INDEX_PAGES:
            group_key = parent_path
        elif parent_dir in SYNTHETIC_REFERENCE_INDEX_DIRS:
            group_key = parent_dir
        else:
            continue
        flat_child_paths_by_parent.setdefault(group_key, []).append(source_path)

    for parent_key, child_paths in sorted(flat_child_paths_by_parent.items()):
        indexed_paths = compact_index_paths_by_parent.get(parent_key, set())
        remaining_child_paths = [
            child_path for child_path in child_paths if child_path not in indexed_paths
        ]
        if not remaining_child_paths:
            continue

        parent_title = ""
        parent_markdown_path = f"{parent_key}.md" if not parent_key.endswith(".md") else parent_key
        if parent_markdown_path in available_source_paths:
            parent_markdown = (input_dir / parent_markdown_path).read_text(encoding="utf-8")
            parent_heading = parse_heading_tree(parent_markdown).children
            parent_title = next(
                (
                    unescape_markdown_text(extract_heading_text(node.heading or "") or "")
                    for node in parent_heading
                    if node.level == 1
                ),
                "",
            )
        if not parent_title:
            parent_title = Path(parent_key).name.replace("-", " ").title()

        links: list[str] = []
        for child_path in remaining_child_paths:
            child_markdown = (input_dir / child_path).read_text(encoding="utf-8")
            child_heading_nodes = parse_heading_tree(child_markdown).children
            child_title = next(
                (
                    unescape_markdown_text(extract_heading_text(node.heading or "") or "")
                    for node in child_heading_nodes
                    if node.level == 1
                ),
                "",
            )
            if not child_title:
                child_title = Path(child_path).stem.replace("-", " ").title()
            links.append(f"[{child_title}]({child_path})")

        if not links:
            continue
        if parent_key in compact_index_nodes_by_parent:
            compact_index_nodes_by_parent[parent_key].children.append(
                Node(
                    heading=f"{'#' * category_level} Additional Pages",
                    level=category_level,
                    content_lines=[f"- {link}" for link in links],
                    preserve_bullets=True,
                )
            )
            continue
        index_nodes.append(
            Node(
                heading=f"{'#' * flat_index_level} {parent_title} Index",
                level=flat_index_level,
                content_lines=[f"- {link}" for link in links],
                preserve_bullets=True,
            )
        )
    return index_nodes
def collect_markdown_files(directory: Path, *, root_dir: Path | None = None) -> list[str]:
    root = root_dir or directory
    files: list[str] = []
    for path in sorted(directory.rglob("*.md")):
        if path.is_file():
            files.append(path.relative_to(root).as_posix())
    return files


def write_skill_files(input_dir: Path, output_dir: Path, source_paths: list[str]) -> int:
    available_source_paths = build_available_source_paths(source_paths)
    count = 0
    for source_path in source_paths:
        if is_excluded_source_path(source_path):
            continue
        source_file = input_dir / source_path
        dest_file = output_dir / source_path
        rewritten = rewrite_content(
            source_file.read_text(encoding="utf-8"),
            source_path,
            available_source_paths,
        )
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        dest_file.write_text(rewritten, encoding="utf-8")
        count += 1
    return count


def create_skill_frontmatter() -> str:
    return (
        "---\n"
        "name: tenzir-docs\n"
        "description: >-\n"
        "  Answer questions using the Tenzir documentation. Use whenever the user asks\n"
        "  about TQL syntax, pipeline operators, functions, data parsing or\n"
        "  transformation, normalization, OCSF mapping, enrichment, lookup tables,\n"
        "  contexts, packages, nodes, platform setup, deployment, configuration,\n"
        "  integrations with tools like Splunk, Kafka, S3, Elasticsearch, or any other\n"
        "  Tenzir feature. Also use when the user asks how to collect, route, filter,\n"
        "  aggregate, or export security data with Tenzir, or needs help writing or\n"
        "  debugging TQL pipelines, even if they don't mention 'Tenzir' explicitly but\n"
        "  are clearly working in a Tenzir context.\n"
        "---\n\n"
    )


def generate_skill_markdown(
    input_dir: Path,
    sitemap_root: Node,
    available_source_paths: set[str],
) -> str:
    title_node = next((child for child in sitemap_root.children if child.level == 1), None)
    if title_node is None:
        raise ValueError("Could not find the sitemap title in sitemap.md.")

    # Build the navigation and examples sections that precede the doc map.
    preamble: list[Node] = [create_navigation_node(), create_examples_node()]

    filtered_children: list[Node] = []
    for section in title_node.children:
        section_name = extract_heading_text(section.heading or "")
        max_depth = SECTION_MAX_LEVEL.get(section_name or "")
        if not max_depth:
            continue
        filtered = filter_node(section, max_depth=max_depth)
        if filtered is not None:
            if section_name == "Reference":
                # Only inline small indexes (node, platform); operator and
                # function indexes live in their own extracted files.
                filtered.children.extend(
                    build_reference_index_nodes(
                        input_dir,
                        filtered.level,
                        available_source_paths,
                        skip_compact_indexes=True,
                    )
                )
                # Add a pointer so the model knows where to find the full
                # operator and function listings.
                pointer_level = min(6, filtered.level + 1)
                filtered.children.append(
                    Node(
                        heading=f"{'#' * pointer_level} Indexes",
                        level=pointer_level,
                        content_lines=[
                            "",
                            "For the complete operator listing by category, read "
                            "[Operator Index](reference/operators-index.md).",
                            "",
                            "For the complete function listing by category, read "
                            "[Function Index](reference/functions-index.md).",
                        ],
                    )
                )
            filtered_children.append(filtered)

    # Strip description paragraphs from deeply nested headings to keep
    # SKILL.md compact while preserving the navigable heading links.
    for child in filtered_children:
        strip_deep_content(child, threshold=SKILL_CONTENT_THRESHOLD)

    filtered_title = Node(
        heading=title_node.heading,
        level=title_node.level,
        content_lines=list(title_node.content_lines),
        children=preamble + filtered_children,
    )
    return re.sub(
        r"\n{3,}",
        "\n\n",
        f"{create_skill_frontmatter()}{render_node(filtered_title, available_source_paths=available_source_paths)}",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    sitemap_path = input_dir / "sitemap.md"

    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    if not sitemap_path.exists():
        raise FileNotFoundError(f"Missing sitemap.md in {input_dir}")

    sitemap_root = parse_heading_tree(sitemap_path.read_text(encoding="utf-8"))
    markdown_files = [
        file_path for file_path in collect_markdown_files(input_dir) if file_path != "sitemap.md"
    ]
    available_source_paths = build_available_source_paths(markdown_files)

    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    skill_md = generate_skill_markdown(input_dir, sitemap_root, available_source_paths)
    (output_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
    copied = write_skill_files(input_dir, output_dir, markdown_files)

    # Generate extracted index files (operator and function listings).
    index_count = 0
    for source_path, (output_path, title) in EXTRACTED_INDEX_FILES.items():
        content = generate_extracted_index(
            input_dir, source_path, title, output_path, available_source_paths,
        )
        if content:
            dest = output_dir / output_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
            index_count += 1

    print(f"Generated {output_dir}/SKILL.md")
    print(f"Copied {copied} markdown files into {output_dir}/")
    print(f"Generated {index_count} extracted index files")


if __name__ == "__main__":
    main()
