#!/usr/bin/env node

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";

const OCSF_SCHEMA_REPO = "https://github.com/ocsf/ocsf-schema.git";
const OCSF_DOCS_API = "https://api.github.com/repos/ocsf/ocsf-docs/contents";
const OCSF_DOCS_RAW = "https://raw.githubusercontent.com/ocsf/ocsf-docs/main";

function versionToSlug(version) {
  return version.replace(/\./g, "-");
}

function nameToSlug(name) {
  return name.replace(/\//g, "_");
}

function cleanDescription(text) {
  if (!text) return "";
  return text
    .replace(/<code>/g, "`")
    .replace(/<\/code>/g, "`")
    .replace(/<a[^>]*href=['"](https?:\/\/[^'"]+)['"][^>]*>([^<]+)<\/a>/g, "[$2]($1)")
    .replace(/<a[^>]*href=['"][^'"]*['"][^>]*>([^<]+)<\/a>/g, "$1")
    .replace(/<li[^>]*>/g, "\n- ")
    .replace(/<\/li>/g, "")
    .replace(/<\/?ul[^>]*>/g, "")
    .replace(/<\/?ol[^>]*>/g, "")
    .replace(/<p[^>]*>/g, "\n\n")
    .replace(/<\/p>/g, "")
    .replace(/<br\s*\/?>/g, "\n")
    .replace(/<[^>]+>/g, "")
    .replace(/\n{3,}/g, "\n\n")
    .replace(/[ \t]+$/gm, "")
    .trim();
}

function formatMetaList(entries) {
  return entries
    .filter(([, value]) => value !== undefined && value !== null && value !== "")
    .map(([label, value]) => `- **${label}**: ${value}`)
    .join("\n");
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf-8"));
}

function writeFile(filePath, content) {
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, content);
}

function listStableVersions() {
  const output = execFileSync("git", ["ls-remote", "--tags", OCSF_SCHEMA_REPO], {
    encoding: "utf-8",
  });
  const versions = new Set();
  for (const line of output.split("\n")) {
    const ref = line.trim().split(/\s+/)[1];
    if (!ref || ref.endsWith("^{}")) continue;
    const match = ref.match(/^refs\/tags\/v?(\d+\.\d+\.\d+)$/);
    if (match && Number.parseInt(match[1].split(".")[0], 10) >= 1) {
      versions.add(match[1]);
    }
  }
  return [...versions].sort((a, b) => {
    const pa = a.split(".").map(Number);
    const pb = b.split(".").map(Number);
    return pa[0] - pb[0] || pa[1] - pb[1] || pa[2] - pb[2];
  });
}

function cloneSchema(version, tempRoot) {
  const repoDir = path.join(tempRoot, `ocsf-schema-${version}`);
  const refs = [`v${version}`, version];
  let cloned = false;
  for (const ref of refs) {
    try {
      execFileSync("git", ["clone", "--depth", "1", "--branch", ref, OCSF_SCHEMA_REPO, repoDir], {
        stdio: "ignore",
      });
      cloned = true;
      break;
    } catch {
      // Try the next ref name.
    }
  }
  if (!cloned) {
    throw new Error(`Failed to clone OCSF schema for version ${version}`);
  }
  return repoDir;
}

function loadDirectoryJson(dir) {
  const result = {};
  if (!fs.existsSync(dir)) return result;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isFile() || !entry.name.endsWith(".json")) continue;
    const key = entry.name.replace(/\.json$/, "");
    result[key] = readJson(path.join(dir, entry.name));
  }
  return result;
}

function loadClasses(schemaDir) {
  const classes = {};
  const eventsDir = path.join(schemaDir, "events");
  if (!fs.existsSync(eventsDir)) return classes;

  const baseEventPath = path.join(eventsDir, "base_event.json");
  if (fs.existsSync(baseEventPath)) {
    classes.base_event = readJson(baseEventPath);
  }

  for (const categoryDir of fs.readdirSync(eventsDir, { withFileTypes: true })) {
    if (!categoryDir.isDirectory()) continue;
    const categoryKey = categoryDir.name;
    const fullDir = path.join(eventsDir, categoryKey);
    for (const entry of fs.readdirSync(fullDir, { withFileTypes: true })) {
      if (!entry.isFile() || !entry.name.endsWith(".json")) continue;
      const className = entry.name.replace(/\.json$/, "");
      if (className === categoryKey) continue;
      const data = readJson(path.join(fullDir, entry.name));
      data.category_key = categoryKey;
      classes[className] = data;
    }
  }

  return classes;
}

function loadExtensions(schemaDir) {
  const result = {};
  const extensionsDir = path.join(schemaDir, "extensions");
  if (!fs.existsSync(extensionsDir)) return result;

  for (const entry of fs.readdirSync(extensionsDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const extDir = path.join(extensionsDir, entry.name);
    const metaPath = path.join(extDir, "extension.json");
    if (!fs.existsSync(metaPath)) continue;
    result[entry.name] = {
      meta: readJson(metaPath),
      objects: loadDirectoryJson(path.join(extDir, "objects")),
      profiles: loadDirectoryJson(path.join(extDir, "profiles")),
      events: loadDirectoryJson(path.join(extDir, "events")),
    };
  }

  return result;
}

function resolveAttribute(name, localData, dictionary) {
  const base = dictionary.attributes?.[name] ?? {};
  return {
    ...base,
    ...localData,
  };
}

function formatAttribute(name, data) {
  const desc = cleanDescription(data.description || data.caption || "");
  const lines = [`### \`${name}\``, ""];
  const meta = formatMetaList([
    ["Type", data.object_type ? `\`${data.object_type}\`` : data.type ? `\`${data.type}\`` : ""],
    ["Requirement", data.requirement],
    ["Observable", data.observable],
    ["Group", data.group],
    ["Sibling", data.sibling ? `\`${data.sibling}\`` : ""],
  ]);
  if (meta) lines.push(meta, "");
  if (Array.isArray(data.range)) {
    lines.push(`- **Range**: \`${data.range[0]}\` to \`${data.range[1]}\``, "");
  }
  if (data.regex) {
    lines.push(`- **Regex**: \`${data.regex}\``, "");
  }
  if (Array.isArray(data.values) && data.values.length > 0) {
    lines.push(`- **Values**: ${data.values.map((value) => `\`${value}\``).join(", ")}`, "");
  }
  if (data.enum && Object.keys(data.enum).length > 0) {
    lines.push("#### Enum values", "");
    for (const [key, value] of Object.entries(data.enum)) {
      const enumDesc = cleanDescription(value.description || "");
      lines.push(`- \`${key}\`: \`${value.caption || key}\`${enumDesc ? ` - ${enumDesc}` : ""}`);
    }
    lines.push("");
  }
  if (desc) lines.push(desc, "");
  return lines.join("\n");
}

function renderEntityPage({ title, description, metaEntries, attributes }) {
  const lines = [`# ${title}`, ""];
  if (description) lines.push(cleanDescription(description), "");
  const meta = formatMetaList(metaEntries);
  if (meta) lines.push(meta, "");
  if (attributes.length > 0) {
    lines.push("## Attributes", "");
    for (const [attrName, attrData] of attributes) {
      lines.push(formatAttribute(attrName, attrData));
    }
  }
  return `${lines.join("\n").replace(/\n{3,}/g, "\n\n").trim()}\n`;
}

function buildVersionDocs(version, schemaDir) {
  const slug = versionToSlug(version);
  const categories = readJson(path.join(schemaDir, "categories.json")).attributes ?? {};
  const dictionary = readJson(path.join(schemaDir, "dictionary.json"));
  const classes = loadClasses(schemaDir);
  const objects = loadDirectoryJson(path.join(schemaDir, "objects"));
  const profiles = loadDirectoryJson(path.join(schemaDir, "profiles"));
  const extensions = loadExtensions(schemaDir);
  const types = dictionary.types?.attributes ?? {};

  return {
    version,
    slug,
    categories,
    dictionary,
    classes,
    objects,
    profiles,
    extensions,
    types,
  };
}

function generateClassesOverview(versionData) {
  const lines = [`# Classes (${versionData.version})`, ""];
  for (const [categoryKey, category] of Object.entries(versionData.categories)) {
    const categoryClasses = Object.entries(versionData.classes)
      .filter(([, data]) => data.category_key === categoryKey)
      .sort((a, b) => (a[1].caption || a[0]).localeCompare(b[1].caption || b[0]));
    if (categoryClasses.length === 0) continue;
    lines.push(`## ${category.caption}`, "", cleanDescription(category.description || ""), "");
    for (const [name, data] of categoryClasses) {
      lines.push(`- [${data.caption || name}](classes/${nameToSlug(name)}.md)`);
    }
    lines.push("");
  }
  if (versionData.classes.base_event) {
    lines.push("## Base Event", "", "- [Base Event](classes/base_event.md)", "");
  }
  return `${lines.join("\n").replace(/\n{3,}/g, "\n\n").trim()}\n`;
}

function generateObjectsOverview(versionData) {
  const lines = [`# Objects (${versionData.version})`, ""];
  for (const [name, data] of Object.entries(versionData.objects).sort((a, b) =>
    (a[1].caption || a[0]).localeCompare(b[1].caption || b[0]),
  )) {
    lines.push(`- [${data.caption || name}](objects/${nameToSlug(name)}.md)`);
  }
  return `${lines.join("\n")}\n`;
}

function generateProfilesOverview(versionData) {
  const lines = [`# Profiles (${versionData.version})`, ""];
  for (const [name, data] of Object.entries(versionData.profiles).sort((a, b) =>
    (a[1].caption || a[0]).localeCompare(b[1].caption || b[0]),
  )) {
    lines.push(`- [${data.caption || name}](profiles/${nameToSlug(name)}.md)`);
  }
  return `${lines.join("\n")}\n`;
}

function generateExtensionsOverview(versionData) {
  const lines = [`# Extensions (${versionData.version})`, ""];
  for (const [name, data] of Object.entries(versionData.extensions).sort((a, b) =>
    (a[1].meta.caption || a[0]).localeCompare(b[1].meta.caption || b[0]),
  )) {
    lines.push(`- [${data.meta.caption || name}](extensions/${nameToSlug(name)}.md)`);
  }
  return `${lines.join("\n")}\n`;
}

function generateTypesOverview(versionData) {
  const lines = [`# Types (${versionData.version})`, ""];
  for (const [name, data] of Object.entries(versionData.types).sort((a, b) =>
    (a[1].caption || a[0]).localeCompare(b[1].caption || b[0]),
  )) {
    lines.push(`## \`${name}\``, "", `- **Caption**: ${data.caption || name}`);
    if (data.type_name) lines.push(`- **Base type**: \`${data.type_name}\``);
    if (data.regex) lines.push(`- **Regex**: \`${data.regex}\``);
    if (Array.isArray(data.range)) {
      lines.push(`- **Range**: \`${data.range[0]}\` to \`${data.range[1]}\``);
    }
    if (Array.isArray(data.values) && data.values.length > 0) {
      lines.push(`- **Values**: ${data.values.map((value) => `\`${value}\``).join(", ")}`);
    }
    const desc = cleanDescription(data.description || "");
    if (desc) lines.push("", desc);
    lines.push("");
  }
  return `${lines.join("\n").replace(/\n{3,}/g, "\n\n").trim()}\n`;
}

function generateVersionOverview(versionData) {
  const lines = [`# OCSF ${versionData.version}`, ""];
  lines.push(`- **Classes**: ${Object.keys(versionData.classes).length}`);
  lines.push(`- **Objects**: ${Object.keys(versionData.objects).length}`);
  lines.push(`- **Profiles**: ${Object.keys(versionData.profiles).length}`);
  lines.push(`- **Extensions**: ${Object.keys(versionData.extensions).length}`);
  lines.push(`- **Types**: ${Object.keys(versionData.types).length}`, "");
  lines.push(`- [Classes](${versionData.slug}/classes.md)`);
  lines.push(`- [Objects](${versionData.slug}/objects.md)`);
  lines.push(`- [Profiles](${versionData.slug}/profiles.md)`);
  lines.push(`- [Extensions](${versionData.slug}/extensions.md)`);
  lines.push(`- [Types](${versionData.slug}/types.md)`, "");
  return `${lines.join("\n")}\n`;
}

async function fetchJson(url) {
  const response = await fetch(url, {
    headers: {
      "User-Agent": "tenzir-skills-generator",
      Accept: "application/json",
    },
  });
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}: HTTP ${response.status}`);
  }
  return await response.json();
}

async function fetchText(url) {
  const response = await fetch(url, {
    headers: {
      "User-Agent": "tenzir-skills-generator",
    },
  });
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}: HTTP ${response.status}`);
  }
  return await response.text();
}

function parseHeading(markdown, fallback) {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : fallback;
}

async function fetchFaqs() {
  const items = await fetchJson(`${OCSF_DOCS_API}/faqs`);
  const pages = [];
  for (const item of items) {
    if (!item.name.endsWith(".md") || item.name.toLowerCase() === "readme.md") continue;
    const content = await fetchText(`${OCSF_DOCS_RAW}/faqs/${item.name}`);
    pages.push({
      slug: item.name.replace(/\.md$/, ""),
      title: parseHeading(content, item.name.replace(/\.md$/, "")),
      content,
    });
  }
  return pages;
}

async function fetchArticles() {
  const items = await fetchJson(`${OCSF_DOCS_API}/articles`);
  const pages = [];
  for (const item of items) {
    if (!item.name.endsWith(".md") || item.name.toLowerCase() === "readme.md") continue;
    const content = await fetchText(`${OCSF_DOCS_RAW}/articles/${item.name}`);
    pages.push({
      slug: item.name.replace(/\.md$/, ""),
      title: parseHeading(content, item.name.replace(/\.md$/, "")),
      content,
    });
  }
  return pages;
}

async function fetchOverview() {
  return await fetchText(`${OCSF_DOCS_RAW}/overview/understanding-ocsf.md`);
}

function parseArgs(argv) {
  const args = {
    outputDir: null,
    version: null,
    latestOnly: false,
  };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--output-dir") args.outputDir = argv[++i];
    if (argv[i] === "--version") args.version = argv[++i];
    if (argv[i] === "--latest-only") args.latestOnly = true;
  }
  if (!args.outputDir) {
    throw new Error("Usage: node scripts/generate-ocsf-skill.mjs --output-dir <dir> [--version <x.y.z>|--latest-only]");
  }
  return args;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  let versions = args.version ? [args.version] : listStableVersions();
  if (args.latestOnly) versions = [versions.at(-1)];

  const outputDir = path.resolve(args.outputDir);
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "ocsf-skill-"));
  const versionDocs = [];

  try {
    for (const version of versions) {
      const schemaDir = cloneSchema(version, tempRoot);
      versionDocs.push(buildVersionDocs(version, schemaDir));
    }

    const latest = versionDocs.at(-1);
    const faqs = await fetchFaqs();
    const articles = await fetchArticles();
    const overview = await fetchOverview();

    fs.rmSync(outputDir, { recursive: true, force: true });
    ensureDir(outputDir);

    writeFile(
      path.join(outputDir, "SKILL.md"),
      [
        "---",
        "name: ocsf",
        "description: Answer questions about OCSF (Open Cybersecurity Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, extensions, or event normalization.",
        "---",
        "",
        "# OCSF",
        "",
        "Look up OCSF reference documentation and answer from those sources. Only state facts from files you read. Never invent schema details. If the documentation does not cover the question, say so.",
        "",
        "## Reading the documentation",
        "",
        "Start with [index.md](index.md) to discover available versions. Use the latest stable version unless the user requests a specific one. Stick to one version per answer.",
        "",
        "The file tree follows this layout:",
        "",
        "```",
        "index.md",
        "introduction.md",
        "faqs.md",
        "faqs/{slug}.md",
        "articles.md",
        "articles/{slug}.md",
        "{version}.md",
        "{version}/classes.md",
        "{version}/classes/{name}.md",
        "{version}/objects.md",
        "{version}/objects/{name}.md",
        "{version}/profiles.md",
        "{version}/profiles/{name}.md",
        "{version}/extensions.md",
        "{version}/extensions/{name}.md",
        "{version}/types.md",
        "```",
        "",
        "## Domain knowledge",
        "",
        "### Core concepts",
        "",
        "**Attributes** are named fields with a data type. Every OCSF field has a requirement level: required, recommended, or optional.",
        "",
        "**Objects** group related attributes into reusable structures. Objects can nest other objects.",
        "",
        "**Event classes** define schemas for specific security events. Each class belongs to a category and inherits from Base Event.",
        "",
        "**Base Event** provides universal attributes and serves as a catch-all when no more specific class fits.",
        "",
        "**Profiles** are mix-ins that add cross-cutting attributes. A class can apply multiple profiles.",
        "",
        "**Extensions** add vendor-specific attributes without modifying the core schema.",
        "",
        "### Event categories",
        "",
        "| Range | Category | Focus |",
        "| ----- | -------- | ----- |",
        "| 1xxx | System Activity | OS-level: process, file, module, memory, kernel, registry |",
        "| 2xxx | Findings | Detections, vulnerabilities, incidents, compliance |",
        "| 3xxx | IAM | Authentication, authorization, account and group changes |",
        "| 4xxx | Network Activity | General traffic and protocol-specific activity |",
        "| 5xxx | Discovery | Device, user, service, and resource enumeration |",
        "| 6xxx | Application Activity | Web resources, API calls, file hosting, datastore operations |",
        "| 7xxx | Remediation | File, process, network, and entity remediation actions |",
        "| 8xxx | Unmanned | Drones, vehicles, and robots |",
        "",
        "### Naming conventions",
        "",
        "- `snake_case` everywhere: `process_activity`, `network_endpoint`.",
        "- Suffixes carry meaning: `_id`, `_uid`, `_uuid`, `_name`, `_time`, `_dt`.",
        "",
        "## Answering principles",
        "",
        "- Read before answering. Every claim must trace back to a file you read.",
        "- Use the category table to narrow scope before diving into class pages.",
        "- Consult [faqs.md](faqs.md) when the question is about schema choices or ambiguity.",
        "- Read multiple candidates for selection questions and explain trade-offs.",
        "",
        "## Documentation map",
        "",
        `### [Introduction](introduction.md)`,
        "",
        `### [Latest classes](${latest.slug}/classes.md)`,
        "",
        `### [Latest objects](${latest.slug}/objects.md)`,
        "",
        `### [Latest profiles](${latest.slug}/profiles.md)`,
        "",
        `### [Latest extensions](${latest.slug}/extensions.md)`,
        "",
        `### [Latest types](${latest.slug}/types.md)`,
        "",
        "### [FAQs](faqs.md)",
        "",
        "### [Articles](articles.md)",
        "",
      ].join("\n"),
    );

    writeFile(
      path.join(outputDir, "index.md"),
      [
        "# OCSF",
        "",
        "Generated from the official [`ocsf-schema`](https://github.com/ocsf/ocsf-schema) and [`ocsf-docs`](https://github.com/ocsf/ocsf-docs) repositories.",
        "",
        "## Versions",
        "",
        ...versionDocs.map((data) => `- [${data.version}](${data.slug}.md)`),
        "",
      ].join("\n"),
    );

    writeFile(path.join(outputDir, "introduction.md"), overview.endsWith("\n") ? overview : `${overview}\n`);

    writeFile(
      path.join(outputDir, "faqs.md"),
      ["# FAQs", "", ...faqs.map((page) => `- [${page.title}](faqs/${page.slug}.md)`), ""].join("\n"),
    );
    for (const faq of faqs) {
      writeFile(path.join(outputDir, "faqs", `${faq.slug}.md`), faq.content.endsWith("\n") ? faq.content : `${faq.content}\n`);
    }

    writeFile(
      path.join(outputDir, "articles.md"),
      ["# Articles", "", ...articles.map((page) => `- [${page.title}](articles/${page.slug}.md)`), ""].join("\n"),
    );
    for (const article of articles) {
      writeFile(path.join(outputDir, "articles", `${article.slug}.md`), article.content.endsWith("\n") ? article.content : `${article.content}\n`);
    }

    for (const data of versionDocs) {
      writeFile(path.join(outputDir, `${data.slug}.md`), generateVersionOverview(data));
      writeFile(path.join(outputDir, data.slug, "classes.md"), generateClassesOverview(data));
      writeFile(path.join(outputDir, data.slug, "objects.md"), generateObjectsOverview(data));
      writeFile(path.join(outputDir, data.slug, "profiles.md"), generateProfilesOverview(data));
      writeFile(path.join(outputDir, data.slug, "extensions.md"), generateExtensionsOverview(data));
      writeFile(path.join(outputDir, data.slug, "types.md"), generateTypesOverview(data));

      for (const [name, classData] of Object.entries(data.classes)) {
        const page = renderEntityPage({
          title: `${classData.caption || name} (${name})`,
          description: classData.description,
          metaEntries: [
            ["UID", classData.uid ? `\`${classData.uid}\`` : ""],
            [
              "Category",
              classData.category_key
                ? data.categories[classData.category_key]?.caption || classData.category_key
                : "",
            ],
            ["Extends", classData.extends ? `\`${classData.extends}\`` : ""],
          ],
          attributes: Object.entries(classData.attributes ?? {}).map(([attrName, attrData]) => [
            attrName,
            resolveAttribute(attrName, attrData, data.dictionary),
          ]),
        });
        writeFile(path.join(outputDir, data.slug, "classes", `${nameToSlug(name)}.md`), page);
      }

      for (const [name, objectData] of Object.entries(data.objects)) {
        const page = renderEntityPage({
          title: `${objectData.caption || name} (${name})`,
          description: objectData.description,
          metaEntries: [["Extends", objectData.extends ? `\`${objectData.extends}\`` : ""]],
          attributes: Object.entries(objectData.attributes ?? {}).map(([attrName, attrData]) => [
            attrName,
            resolveAttribute(attrName, attrData, data.dictionary),
          ]),
        });
        writeFile(path.join(outputDir, data.slug, "objects", `${nameToSlug(name)}.md`), page);
      }

      for (const [name, profileData] of Object.entries(data.profiles)) {
        const page = renderEntityPage({
          title: `${profileData.caption || name} (${name})`,
          description: profileData.description,
          metaEntries: [],
          attributes: Object.entries(profileData.attributes ?? {}).map(([attrName, attrData]) => [
            attrName,
            resolveAttribute(attrName, attrData, data.dictionary),
          ]),
        });
        writeFile(path.join(outputDir, data.slug, "profiles", `${nameToSlug(name)}.md`), page);
      }

      for (const [name, extensionData] of Object.entries(data.extensions)) {
        const lines = [`# ${extensionData.meta.caption || name}`, ""];
        const desc = cleanDescription(extensionData.meta.description || "");
        if (desc) lines.push(desc, "");
        lines.push(`- **Name**: \`${extensionData.meta.name || name}\``);
        if (extensionData.meta.uid !== undefined) {
          lines.push(`- **UID**: \`${extensionData.meta.uid}\``);
        }
        lines.push("");
        if (Object.keys(extensionData.events).length > 0) {
          lines.push("## Events", "");
          for (const [eventName, eventData] of Object.entries(extensionData.events).sort((a, b) =>
            (a[1].caption || a[0]).localeCompare(b[1].caption || b[0]),
          )) {
            lines.push(`- \`${eventName}\`${eventData.caption ? ` - ${eventData.caption}` : ""}`);
          }
          lines.push("");
        }
        if (Object.keys(extensionData.objects).length > 0) {
          lines.push("## Objects", "");
          for (const [objectName, objectData] of Object.entries(extensionData.objects).sort((a, b) =>
            (a[1].caption || a[0]).localeCompare(b[1].caption || b[0]),
          )) {
            lines.push(`- \`${objectName}\`${objectData.caption ? ` - ${objectData.caption}` : ""}`);
          }
          lines.push("");
        }
        if (Object.keys(extensionData.profiles).length > 0) {
          lines.push("## Profiles", "");
          for (const [profileName, profileData] of Object.entries(extensionData.profiles).sort((a, b) =>
            (a[1].caption || a[0]).localeCompare(b[1].caption || b[0]),
          )) {
            lines.push(`- \`${profileName}\`${profileData.caption ? ` - ${profileData.caption}` : ""}`);
          }
          lines.push("");
        }
        writeFile(path.join(outputDir, data.slug, "extensions", `${nameToSlug(name)}.md`), `${lines.join("\n")}\n`);
      }
    }

    console.log(`Generated OCSF skill in ${outputDir}`);
  } finally {
    fs.rmSync(tempRoot, { recursive: true, force: true });
  }
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
});
