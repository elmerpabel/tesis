#!/usr/bin/env python3
"""
Importa un archivo Markdown generado por el skill `tesis` como documento nativo de Google Docs
y lo ubica en la carpeta de destino especificada en Google Drive.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"Error ejecutando {' '.join(cmd)} (code {proc.returncode}):\n{proc.stderr.strip()}"
        )
    return proc.stdout + "\n" + proc.stderr


def extract_doc_info(output: str) -> tuple[str, str]:
    url_match = re.search(r"(https://docs\.google\.com/document/d/([A-Za-z0-9_-]+)/[^\s]*)", output)
    if url_match:
        return url_match.group(2), url_match.group(1)
    id_match = re.search(r"ID:\s*([A-Za-z0-9_-]+)", output)
    if id_match:
        doc_id = id_match.group(1)
        return doc_id, f"https://docs.google.com/document/d/{doc_id}/edit"
    raise RuntimeError(f"No se pudo detectar el ID del Google Doc creado:\n{output}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convierte un archivo Markdown a Google Docs y lo mueve a la carpeta de tesis en Drive."
    )
    parser.add_argument("--md-file", required=True, help="Ruta local al archivo Markdown.")
    parser.add_argument("--title", required=True, help="Título del documento Google Docs.")
    parser.add_argument(
        "--folder-id",
        required=True,
        help="ID de la carpeta destino en Google Drive (ej. subcarpeta 01_Estructura_y_Borradores).",
    )
    parser.add_argument(
        "--paged",
        action="store_true",
        help="Usar formato paginado en lugar del formato sin páginas por defecto.",
    )
    parser.add_argument(
        "--upload-md-backup",
        action="store_true",
        help="Sube además una copia del archivo .md original en la misma carpeta.",
    )
    args = parser.parse_args()

    md_path = Path(args.md_file).expanduser().resolve()
    if not md_path.is_file():
        print(
            json.dumps({"error": f"Archivo no encontrado: {md_path}"}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 1

    try:
        cmd = [
            "gdocs",
            "mutate",
            "import-md",
            str(md_path),
            "--title",
            args.title,
            "--auto-fit-tables",
        ]
        if args.paged:
            cmd.append("--pageless=false")

        import_out = run_cmd(cmd)
        doc_id, doc_url = extract_doc_info(import_out)

        run_cmd(["gdrive", "mutate", "mv", doc_id, args.folder_id])

        result = {
            "title": args.title,
            "doc_id": doc_id,
            "url": doc_url,
            "folder_id": args.folder_id,
            "folder_url": f"https://drive.google.com/drive/folders/{args.folder_id}",
        }

        if args.upload_md_backup:
            run_cmd(["gdrive", "mutate", "upload", str(md_path), "--parent", args.folder_id])
            result["md_backup_uploaded"] = True

        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
