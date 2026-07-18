import importlib
import json
import tempfile
import unittest
from pathlib import Path


MODULE = importlib.import_module("scripts.research.notebooklm_import")


class NotebookLmImportTests(unittest.TestCase):
    def fragment(self, root: Path) -> Path:
        fragment = root / "fragment"
        fragment.mkdir()
        note = "---\ntype: research-notebooklm\n---\n\n# Curso\n\n## 1. Sumário Executivo\n\nResumo.\n\n## Mapa mental\n\n```mermaid\nmindmap\n  root((Curso))\n```\n\n## Fontes originais\n\n- [Fonte](https://example.com)\n"
        (fragment / "note.md").write_text(note, encoding="utf-8")
        (fragment / "manifest.json").write_text(json.dumps({"contract_version": "1", "profile": "okf-fragment", "note": "note.md", "notebook_id": "n1", "source_links": [{"title": "Fonte", "type": "web_page", "notebooklm_source_id": "s1", "url": "https://example.com"}]}), encoding="utf-8")
        return fragment

    def bundle(self, root: Path) -> Path:
        bundle = root / "bundle"
        bundle.mkdir()
        (bundle / "index.md").write_text("---\nokf_version: \"0.1\"\n---\n\n# Índice\n", encoding="utf-8")
        (bundle / "log.md").write_text("# Log\n", encoding="utf-8")
        return bundle

    def test_import_updates_canonical_files(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            result = MODULE.import_fragment(self.fragment(root), self.bundle(root), Path("Research/curso.md"))
            bundle = root / "bundle"
            self.assertEqual(result["saved_note"], "Research/curso.md")
            self.assertIn("[Curso](Research/curso.md)", (bundle / "index.md").read_text(encoding="utf-8"))
            self.assertIn("notebooklm-import", (bundle / "log.md").read_text(encoding="utf-8"))

    def test_invalid_fragment_never_writes_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            fragment = self.fragment(root)
            (fragment / "note.md").write_text("# sem frontmatter\n", encoding="utf-8")
            bundle = self.bundle(root)
            with self.assertRaises(ValueError):
                MODULE.import_fragment(fragment, bundle, Path("Research/curso.md"))
            self.assertFalse((bundle / "Research" / "curso.md").exists())


if __name__ == "__main__":
    unittest.main()
