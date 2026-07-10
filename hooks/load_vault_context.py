#!/usr/bin/env python3
"""SessionStart hook: inject bundle context into the session once per start.

Gated to the AI-Brain vault: fires only when the session's cwd is inside
$OBSIDIAN_VAULT_PATH. Skips silently otherwise (any output would land in
the model's context for non-vault sessions, which is not what we want).

Setup:
    1. Set OBSIDIAN_VAULT_PATH in ~/.claude/settings.json env section
    2. Register as a SessionStart hook in ~/.claude/settings.json:
         { "type": "command",
           "command": "python ~/.claude/skills/obsidian-second-brain/hooks/load_vault_context.py" }

Path normalization handles Windows ("C:\\..."), MSYS ("/c/..."), and POSIX
("/...") - match works regardless of which form the harness or env var uses.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


def normalize(p: str) -> str:
    """Lowercase drive letter, forward slashes, no trailing slash."""
    if not p:
        return ""
    p = p.replace("\\", "/")
    m = re.match(r"^([A-Za-z]):(.*)$", p)
    if m:
        p = f"/{m.group(1).lower()}{m.group(2)}"
    return p.rstrip("/")


def main() -> int:
    vault = os.environ.get("OBSIDIAN_VAULT_PATH", "")
    if not vault:
        return 0

    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    cwd = payload.get("cwd", "")
    vault_n = normalize(vault)
    cwd_n = normalize(cwd)

    if not (cwd_n == vault_n or cwd_n.startswith(vault_n + "/")):
        return 0

    v = Path(vault)
    index_md = v / "index.md"
    claude_md = v / "_CLAUDE.md"
    log_md = v / "log.md"

    if not index_md.is_file() and not claude_md.is_file():
        return 0

    sections: list[str] = []
    key_lines = [f"  - `{index_md}` - canonical bundle entrypoint"]

    if log_md.is_file():
        key_lines.append(f"  - `{log_md}` - canonical operation log")
    if claude_md.is_file():
        key_lines.append(f"  - `{claude_md}` - optional local runtime extension")

    if index_md.is_file():
        sections.append(
            "Bundle index (`index.md`, loaded once at session start - do not re-read on "
            "each command unless the bundle changes):\n\n"
            + index_md.read_text(encoding="utf-8")
        )
    if claude_md.is_file():
        sections.append(
            "Bundle extension (`_CLAUDE.md`, optional local runtime guidance):\n\n"
            + claude_md.read_text(encoding="utf-8")
        )

    header = (
        f"**Vault root**: `{vault}`\n"
        f"**Key files** (absolute paths - use these directly, no discovery needed):\n"
        + "\n".join(key_lines)
        + "\n"
        "**Do NOT run `ls`, `Glob`, or `Bash` to discover the vault or its folders.**\n"
        "Use the vault root path above and the bundle files below directly.\n\n"
        "---\n\n"
    )

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": header + "\n\n---\n\n".join(sections),
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
