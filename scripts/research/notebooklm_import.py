#!/usr/bin/env python3
"""Import a validated notebooklm-to-notes OKF fragment into a host bundle."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path



def read_fragment(fragment: Path) -> tuple[str, dict]:
    note = fragment / "note.md"
    manifest = fragment / "manifest.json"
    if not note.is_file() or not manifest.is_file():
        raise ValueError("fragmento exige note.md e manifest.json")
    raw = note.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("note.md não pode ter BOM")
    text = raw.decode("utf-8")
    if "[[" in text or re.search(r"\]\((?:/|file:)", text):
        raise ValueError("fragmento contém links internos incompatíveis com OKF")
    frontmatter = re.match(
        r"\A---\r?\n(?P<content>.*?)^---\r?\n",
        text,
        re.DOTALL | re.MULTILINE,
    )
    if not frontmatter or not re.search(
        r"^type:[ \t]*\S.*$",
        frontmatter.group("content"),
        re.MULTILINE,
    ):
        raise ValueError("note.md exige frontmatter YAML com type")
    if not re.search(r"^# .+", text, re.MULTILINE):
        raise ValueError("note.md exige H1")
    if "## 1. Sumário Executivo" not in text or not re.search(r"```mermaid\r?\nmindmap\r?\n", text) or "## Fontes originais" not in text:
        raise ValueError("fragmento não contém a estrutura editorial obrigatória")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data.get("contract_version") != "1" or data.get("profile") != "okf-fragment" or data.get("note") != "note.md":
        raise ValueError("manifesto okf-fragment inválido")
    if not isinstance(data.get("source_links"), list) or not data["source_links"]:
        raise ValueError("manifesto exige source_links")
    for source in data["source_links"]:
        if not isinstance(source, dict) or not all(source.get(key) for key in ("title", "type", "notebooklm_source_id")):
            raise ValueError("manifesto contém fonte incompleta")
    return text, data


def title_from(text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else "Importação NotebookLM"


def relative_target(root: Path, destination: Path) -> str:
    try:
        return destination.relative_to(root).as_posix()
    except ValueError as error:
        raise ValueError("destino precisa estar dentro do bundle") from error


def append_index_and_log(root: Path, destination: Path, title: str, notebook_id: str) -> None:
    index, log = root / "index.md", root / "log.md"
    if not index.is_file() or not log.is_file():
        raise ValueError("bundle hospedeiro exige index.md e log.md na raiz")
    rel = relative_target(root, destination)
    index_text = index.read_text(encoding="utf-8")
    link = f"[{title}]({rel})"
    if link not in index_text:
        with index.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(f"\n- {link} — importação do NotebookLM.\n")
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    with log.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(f"\n## {stamp} — notebooklm-import\n\n- Importado {link} do notebook `{notebook_id}`.\n")


def import_fragment(fragment: Path, root: Path, destination: Path) -> dict:
    text, manifest = read_fragment(fragment)
    destination = destination if destination.is_absolute() else root / destination
    relative_target(root, destination)
    if destination.name in {"index.md", "log.md"}:
        raise ValueError("destino não pode ser index.md ou log.md")
    if destination.exists():
        raise FileExistsError(f"destino já existe: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8", newline="\n")
    append_index_and_log(root, destination, title_from(text), str(manifest["notebook_id"]))
    return {"saved_note": relative_target(root, destination), "notebook_id": manifest["notebook_id"], "source_count": len(manifest["source_links"])}


def resolve_exporter() -> str | None:
    configured = os.environ.get("NOTEBOOKLM_TO_NOTES_BIN")
    candidates = [configured] if configured else ["notebooklm-to-notes"]
    for candidate in candidates:
        if candidate and shutil.which(candidate):
            return candidate
    return None


def export_fragment(notebook: str, fragment: Path) -> None:
    binary = resolve_exporter()
    if binary is None:
        raise RuntimeError(
            "notebooklm-to-notes não está disponível. "
            "Instale/configure o exportador antes de usar /notebooklm-import, "
            "ou defina NOTEBOOKLM_TO_NOTES_BIN com o caminho do binário."
        )
    result = subprocess.run(
        [binary, "--profile", "okf-fragment", "--notebook", notebook, "--fragment-dir", str(fragment), "--json"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        raise RuntimeError(stderr or stdout or "exportador notebooklm-to-notes falhou")


def preflight() -> dict:
    configured = os.environ.get("NOTEBOOKLM_TO_NOTES_BIN")
    resolved = resolve_exporter()
    return {
        "status": "ok" if resolved else "missing-exporter",
        "exporter": configured or "notebooklm-to-notes",
        "resolved_path": resolved,
        "next_step": None
        if resolved
        else "Instale notebooklm-to-notes ou defina NOTEBOOKLM_TO_NOTES_BIN antes de importar.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notebook")
    parser.add_argument("--destination", help="caminho .md relativo ao bundle")
    parser.add_argument("--fragment-dir", type=Path, help="fragmento existente para testes ou reimportação")
    parser.add_argument("--preflight", action="store_true", help="verifica dependências locais sem importar")
    args = parser.parse_args()
    if args.preflight:
        print(json.dumps(preflight(), ensure_ascii=False, indent=2))
        return 0
    if not args.notebook or not args.destination:
        parser.error("--notebook e --destination são obrigatórios, exceto com --preflight")
    from .lib.config import VAULT_PATH

    root = VAULT_PATH
    if args.fragment_dir:
        result = import_fragment(args.fragment_dir, root, Path(args.destination))
    else:
        with tempfile.TemporaryDirectory(prefix="notebooklm-import-") as folder:
            fragment = Path(folder)
            export_fragment(args.notebook, fragment)
            result = import_fragment(fragment, root, Path(args.destination))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
