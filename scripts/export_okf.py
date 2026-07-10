# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""
export_okf.py - export a knowledge bundle as OKF-compatible markdown.

The native vault still carries richer second-brain conventions, but the emitted
bundle should be consumable by any tool that understands OKF 0.1: markdown
concept docs with YAML frontmatter, relative markdown links, a root index.md,
and a root log.md.
"""

from __future__ import annotations

import argparse
import datetime
import html
import os
import pathlib
import re
import sys
from collections import OrderedDict

import yaml

FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
WIKILINK_RE = re.compile(r"(!?)\[\[([^\]]+)\]\]")
SKIP_DIRS = {".obsidian", "_export", ".git", ".trash", ".claude", "templates", "Excalidraw"}
RESERVED_FILENAMES = {"index.md", "log.md"}
RESOURCE_KEYS = ("resource", "url", "source_url", "post-url", "post_url", "repo", "linkedin")


def parse_note(text: str) -> tuple[dict, str]:
    match = FM_RE.match(text)
    if match:
        try:
            fm = yaml.safe_load(match.group(1)) or {}
        except Exception:
            fm = {}
        body = match.group(2)
    else:
        fm, body = {}, text
    return (fm if isinstance(fm, dict) else {}), body


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


def first_paragraph(body: str) -> str:
    paragraph: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            if paragraph:
                break
            continue
        if stripped.startswith(("#", ">", "-", "*", "|", "```")):
            if paragraph:
                break
            continue
        paragraph.append(stripped)
    return " ".join(paragraph)


def clean_desc(value: str) -> str:
    def _wikilink_label(match: re.Match[str]) -> str:
        inner = match.group(2)
        display = inner.split("|", 1)[1] if "|" in inner else inner
        return display.split("#", 1)[0].strip()

    value = html.unescape(value)
    value = WIKILINK_RE.sub(_wikilink_label, value)
    value = re.sub(r"[*_`>#]+", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) > 200:
        value = value[:200].rsplit(" ", 1)[0].rstrip(",.;:") + "..."
    return value


def to_iso(frontmatter: dict, src_file: pathlib.Path) -> str:
    date_value = frontmatter.get("date")
    time_value = frontmatter.get("time")
    if date_value:
        date_str = str(date_value)
        if time_value:
            time_str = str(time_value)
            return f"{date_str}T{time_str}:00Z" if len(time_str) <= 5 else f"{date_str}T{time_str}Z"
        return f"{date_str}T00:00:00Z"
    mtime = datetime.datetime.fromtimestamp(src_file.stat().st_mtime, datetime.timezone.utc)
    return mtime.strftime("%Y-%m-%dT%H:%M:%SZ")


def infer_type(frontmatter: dict, rel: str) -> str:
    note_type = frontmatter.get("type")
    if note_type:
        return str(note_type)
    parts = pathlib.PurePath(rel).parts
    if len(parts) >= 2:
        folder = parts[-2].lower()
        singular = {
            "entities": "entity",
            "projects": "project",
            "concepts": "concept",
            "daily": "daily",
            "meetings": "meeting",
            "decisions": "decision",
            "tasks": "task",
            "logs": "log",
        }.get(folder, folder.rstrip("s") or "note")
        return singular
    return "note"


def dump_frontmatter(frontmatter: OrderedDict) -> str:
    return yaml.safe_dump(
        dict(frontmatter),
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--out", default="_export/okf")
    args = parser.parse_args()

    vault = pathlib.Path(args.path).expanduser()
    if not vault.is_dir():
        print(f"vault not found: {vault}", file=sys.stderr)
        sys.exit(1)
    out = (vault / args.out) if not os.path.isabs(args.out) else pathlib.Path(args.out)

    notes: dict[str, tuple[pathlib.Path, dict, str]] = {}
    for file_path in vault.rglob("*.md"):
        rel = file_path.relative_to(vault)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if str(rel).startswith(args.out):
            continue
        if rel.name in RESERVED_FILENAMES:
            continue
        frontmatter, body = parse_note(file_path.read_text(encoding="utf-8", errors="replace"))
        notes[str(rel)] = (file_path, frontmatter, body)

    name_to_rel: dict[str, str] = {}
    for rel, (_, frontmatter, _) in notes.items():
        stem = pathlib.PurePath(rel).stem
        name_to_rel.setdefault(stem.lower(), rel)
        for alias in frontmatter.get("aliases") or []:
            name_to_rel.setdefault(str(alias).lower(), rel)

    def convert_links(body: str, from_rel: str) -> str:
        from_dir = pathlib.PurePath(from_rel).parent

        def repl(match: re.Match[str]) -> str:
            embed, inner = match.group(1), match.group(2)
            target = inner.split("|", 1)[0].split("#", 1)[0].strip()
            display = inner.split("|", 1)[1].strip() if "|" in inner else target
            target_rel = name_to_rel.get(pathlib.PurePath(target).stem.lower())
            if target_rel:
                relpath = os.path.relpath(target_rel, from_dir) if str(from_dir) != "." else target_rel
                relpath = relpath.replace(os.sep, "/")
                href = relpath
                return f"![{display}]({href})" if embed else f"[{display}]({href})"
            href = target
            return f"![{display}]({href})" if embed else display

        return WIKILINK_RE.sub(repl, body)

    out.mkdir(parents=True, exist_ok=True)
    written = 0
    for rel, (src, frontmatter, body) in sorted(notes.items()):
        title = frontmatter.get("title") or first_heading(body) or pathlib.PurePath(rel).stem
        description = clean_desc(str(frontmatter.get("description") or first_paragraph(body)))
        note_type = infer_type(frontmatter, rel)
        tags = frontmatter.get("tags") or []
        resource = next((str(frontmatter[key]) for key in RESOURCE_KEYS if frontmatter.get(key)), None)

        okf_frontmatter: OrderedDict[str, object] = OrderedDict()
        okf_frontmatter["type"] = note_type
        okf_frontmatter["title"] = title
        if description:
            okf_frontmatter["description"] = description
        if resource:
            okf_frontmatter["resource"] = resource
        if tags:
            okf_frontmatter["tags"] = tags
        okf_frontmatter["timestamp"] = to_iso(frontmatter, src)
        for key, value in frontmatter.items():
            if key in okf_frontmatter:
                continue
            okf_frontmatter[key] = value

        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        payload = f"---\n{dump_frontmatter(okf_frontmatter)}\n---\n\n{convert_links(body, rel).lstrip(chr(10))}"
        dest.write_text(payload, encoding="utf-8")
        written += 1

    groups: dict[str, list[str]] = {}
    for rel in notes:
        parts = pathlib.PurePath(rel).parts
        top = parts[0] if len(parts) > 1 else "."
        groups.setdefault(top, []).append(rel)

    index_lines = [
        "---",
        'type: index',
        'okf_version: "0.1"',
        "---",
        "",
        f"# {vault.name} - OKF bundle",
        "",
        f"{written} concepts. Exported by obsidian-second-brain (OKF v0.1 compatible).",
        "",
    ]
    for top in sorted(groups):
        index_lines.append(f"## {top}")
        index_lines.append("")
        for rel in sorted(groups[top]):
            title = pathlib.PurePath(rel).stem
            index_lines.append(f"- [{title}]({rel.replace(os.sep, '/')})")
        index_lines.append("")
    (out / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

    source_log = vault / "log.md"
    if source_log.exists():
        log_content = source_log.read_text(encoding="utf-8", errors="replace")
    else:
        today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        log_content = "# Log\n\n" + f"## {today} export | Generated during OKF export\n"
    (out / "log.md").write_text(log_content, encoding="utf-8")

    print(f"OKF bundle written: {out}")
    print(f"  {written} concept docs + index.md + log.md")


if __name__ == "__main__":
    main()