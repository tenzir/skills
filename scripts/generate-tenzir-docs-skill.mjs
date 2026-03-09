#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const DOCS_URL_PREFIX = /^https?:\/\/docs\.tenzir\.com/;
const OCSF_ROOT = "reference/ocsf";
const CHANGELOG_ROOT = "changelog";

const SECTION_MAX_LEVEL = {
  Guides: 4,
  Tutorials: 4,
  Explanations: 4,
  Integrations: 4,
  Reference: 3,
};

function isOcsfSourcePath(sourcePath) {
  return (
    sourcePath === `${OCSF_ROOT}.md` || sourcePath.startsWith(`${OCSF_ROOT}/`)
  );
}

function isChangelogSourcePath(sourcePath) {
  return (
    sourcePath === `${CHANGELOG_ROOT}.md` ||
    sourcePath.startsWith(`${CHANGELOG_ROOT}/`)
  );
}

function isExcludedSourcePath(sourcePath) {
  return isOcsfSourcePath(sourcePath) || isChangelogSourcePath(sourcePath);
}

function getHeadingLevel(line) {
  const match = line.match(/^(#{1,6})\s/);
  return match ? match[1].length : 0;
}

function extractHeadingText(line) {
  const linkMatch = line.match(/^#{1,6}\s+\[([^\]]+)\]/);
  if (linkMatch) return linkMatch[1];
  const plainMatch = line.match(/^#{1,6}\s+(.+)$/);
  return plainMatch ? plainMatch[1] : null;
}

function extractHeadingHref(line) {
  const match = line.match(/^#{1,6}\s+\[[^\]]+\]\(([^)]+)\)/);
  return match ? match[1] : null;
}

function normalizeRelativePath(filePath) {
  return filePath.split(path.sep).join("/");
}

function normalizeDocsHref(href) {
  if (!href) return href;
  return href.replace(DOCS_URL_PREFIX, "");
}

function toSourceMarkdownPath(href) {
  if (!href) return null;
  const normalized = normalizeDocsHref(href);
  if (!normalized.startsWith("/")) return null;
  const pathPart = normalized.slice(1).split("#")[0].split("?")[0];
  return pathPart.endsWith(".md") ? pathPart : null;
}

function getNodeSourcePath(node) {
  return toSourceMarkdownPath(extractHeadingHref(node.heading ?? ""));
}

function isBulletLine(line) {
  return line.startsWith("- ") || line.startsWith("  - ");
}

function trimBlankLines(lines) {
  let start = 0;
  let end = lines.length;
  while (start < end && lines[start]?.trim() === "") start++;
  while (end > start && lines[end - 1]?.trim() === "") end--;
  return lines.slice(start, end);
}

function hasMeaningfulContent(lines) {
  return lines.some((line) => line.trim() !== "" && !isBulletLine(line));
}

function parseHeadingTree(markdown) {
  const root = {
    heading: null,
    level: 0,
    contentLines: [],
    children: [],
  };
  const stack = [root];

  for (const line of markdown.split("\n")) {
    const level = getHeadingLevel(line);
    if (level === 0) {
      stack.at(-1).contentLines.push(line);
      continue;
    }
    while (stack.at(-1).level >= level) {
      stack.pop();
    }
    const node = {
      heading: line,
      level,
      contentLines: [],
      children: [],
    };
    stack.at(-1).children.push(node);
    stack.push(node);
  }

  return root;
}

function filterNode(node, { maxDepth }) {
  if (node.level > maxDepth) return null;
  const sourcePath = getNodeSourcePath(node);
  if (sourcePath && isExcludedSourcePath(sourcePath)) return null;

  const children = node.children
    .map((child) => filterNode(child, { maxDepth }))
    .filter(Boolean);

  if (
    !children.length &&
    !hasMeaningfulContent(node.contentLines) &&
    !sourcePath
  ) {
    return null;
  }

  return {
    ...node,
    children,
  };
}

function rewriteLinkDestination(href, fromPath) {
  if (
    !href ||
    href.startsWith("#") ||
    href.startsWith("mailto:") ||
    href.startsWith("tel:")
  ) {
    return href;
  }

  const normalized = normalizeDocsHref(href);
  if (!normalized.startsWith("/")) return href;

  const hashIndex = normalized.indexOf("#");
  const queryIndex = normalized.indexOf("?");
  const suffixIndex =
    hashIndex > -1 && queryIndex > -1
      ? Math.min(hashIndex, queryIndex)
      : hashIndex > -1
        ? hashIndex
        : queryIndex > -1
          ? queryIndex
          : normalized.length;

  const pathname = normalized.slice(0, suffixIndex);
  const suffix = normalized.slice(suffixIndex);
  const sourcePath = pathname.slice(1);
  if (!sourcePath.endsWith(".md")) return href;
  if (isExcludedSourcePath(sourcePath)) return null;

  const fromDir =
    path.posix.dirname(fromPath) === "." ? "" : path.posix.dirname(fromPath);
  const relative = path.posix.relative(fromDir || ".", sourcePath) || sourcePath;
  return `${relative}${suffix}`;
}

function rewriteContent(text, fromPath) {
  return text
    .replace(/^> Documentation index:.*\n?/gm, "")
    .replace(/(!?)\[([^\]]*)\]\(([^)]+)\)/g, (_match, bang, label, href) => {
      const rewrittenHref = rewriteLinkDestination(href, fromPath);
      if (rewrittenHref === null) {
        return bang ? `![${label}]` : label;
      }
      return `${bang}[${label}](${rewrittenHref})`;
    });
}

function renderNode(node, { levelOffset = 0, fromPath = "SKILL.md" } = {}) {
  const lines = [];

  if (node.heading) {
    const level = Math.max(1, Math.min(6, node.level + levelOffset));
    const headingText = rewriteContent(node.heading, fromPath).replace(
      /^#{1,6}/,
      "#".repeat(level),
    );
    lines.push(headingText, "");
  }

  const contentLines = trimBlankLines(
    node.contentLines
      .filter((line) => !isBulletLine(line))
      .map((line) => rewriteContent(line, fromPath)),
  );
  if (contentLines.length > 0) {
    lines.push(...contentLines, "");
  }

  for (const child of node.children) {
    const renderedChild = renderNode(child, { levelOffset, fromPath });
    if (renderedChild) lines.push(renderedChild);
  }

  return lines.join("\n");
}

function collectMarkdownFiles(dir, rootDir = dir) {
  const files = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...collectMarkdownFiles(fullPath, rootDir));
      continue;
    }
    if (!entry.name.endsWith(".md")) continue;
    files.push(normalizeRelativePath(path.relative(rootDir, fullPath)));
  }

  return files;
}

function writeSkillFiles(inputDir, outputDir, sourcePaths) {
  let count = 0;
  for (const sourcePath of sourcePaths) {
    if (isExcludedSourcePath(sourcePath)) continue;
    const sourceFile = path.join(inputDir, sourcePath);
    const destFile = path.join(outputDir, sourcePath);
    const content = fs.readFileSync(sourceFile, "utf-8");
    const rewritten = rewriteContent(content, sourcePath);
    fs.mkdirSync(path.dirname(destFile), { recursive: true });
    fs.writeFileSync(destFile, rewritten);
    count++;
  }
  return count;
}

function createSkillFrontmatter() {
  return `---\nname: tenzir-docs\ndescription: Answer questions using the Tenzir documentation. Use when the user asks about TQL, operators, pipelines, packages, nodes, the platform, MCP tools, or documented integrations.\n---\n\n`;
}

function generateSkillMarkdown(sitemapRoot) {
  const titleNode = sitemapRoot.children.find((child) => child.level === 1);
  if (!titleNode) {
    throw new Error("Could not find the sitemap title in sitemap.md.");
  }

  const filteredTitleNode = {
    ...titleNode,
    children: titleNode.children
      .map((section) => {
        const sectionName = extractHeadingText(section.heading ?? "");
        const maxDepth = sectionName ? SECTION_MAX_LEVEL[sectionName] : null;
        if (!maxDepth) return null;
        return filterNode(section, { maxDepth });
      })
      .filter(Boolean),
  };

  return `${createSkillFrontmatter()}${renderNode(filteredTitleNode).replace(/\n{3,}/g, "\n\n")}`;
}

function parseArgs(argv) {
  const args = {
    inputDir: null,
    outputDir: null,
  };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--input-dir") args.inputDir = argv[++i];
    if (argv[i] === "--output-dir") args.outputDir = argv[++i];
  }
  if (!args.inputDir || !args.outputDir) {
    throw new Error("Usage: node scripts/generate-tenzir-docs-skill.mjs --input-dir <dir> --output-dir <dir>");
  }
  return args;
}

function main() {
  const { inputDir, outputDir } = parseArgs(process.argv.slice(2));
  const sitemapPath = path.join(inputDir, "sitemap.md");
  if (!fs.existsSync(inputDir)) {
    throw new Error(`Input directory not found: ${inputDir}`);
  }
  if (!fs.existsSync(sitemapPath)) {
    throw new Error(`Missing sitemap.md in ${inputDir}`);
  }

  const sitemap = fs.readFileSync(sitemapPath, "utf-8");
  const sitemapRoot = parseHeadingTree(sitemap);
  const markdownFiles = collectMarkdownFiles(inputDir).filter(
    (filePath) => filePath !== "sitemap.md",
  );

  if (fs.existsSync(outputDir)) {
    fs.rmSync(outputDir, { recursive: true, force: true });
  }
  fs.mkdirSync(outputDir, { recursive: true });

  const skillMd = generateSkillMarkdown(sitemapRoot);
  fs.writeFileSync(path.join(outputDir, "SKILL.md"), skillMd);
  const copied = writeSkillFiles(inputDir, outputDir, markdownFiles);

  console.log(`Generated ${outputDir}/SKILL.md`);
  console.log(`Copied ${copied} markdown files into ${outputDir}/`);
}

try {
  main();
} catch (error) {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
}
