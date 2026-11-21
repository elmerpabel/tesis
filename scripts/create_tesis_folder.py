#!/usr/bin/env python3
"""
Inicializa una carpeta correlativa para un proyecto de tesis generado con el skill `tesis`.

Formato estándar:
    <NNN>_Tesis_Antigravity_<AcronimoApellido>
    Ejemplo: 001_Tesis_Antigravity_EHuayna

Modos de operación:
  1. Modo Local (por defecto si no se configura TESIS_DRIVE_OUTPUT_FOLDER_ID ni --parent-id)
  2. Modo Google Drive (requiere CLI `gdrive` conectado y --parent-id o TESIS_DRIVE_OUTPUT_FOLDER_ID)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

DEFAULT_DRIVE_OUTPUT_FOLDER_ID = os.environ.get("TESIS_DRIVE_OUTPUT_FOLDER_ID", "")

SUBFOLDERS = [
    "01_Estructura_y_Borradores",
    "02_Marco_Teorico_y_Referencias",
    "03_Metodologia_y_Datos",
    "04_Presentaciones",
    "05_Cronograma_y_Entregables",
]

FOLDER_PATTERN = re.compile(r"^(\d{3})_Tesis_Antigravity_")


def strip_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def normalize_acronym(acronym: str | None, full_name: str | None) -> str:
    """Construye o sanitiza el acrónimo (ej. 'Elmer Huayna' -> 'EHuayna')."""
    if acronym:
        clean = re.sub(r"[^A-Za-z0-9]", "", strip_accents(acronym.strip()))
        if not clean:
            raise ValueError("El acrónimo no puede quedar vacío tras sanitizar.")
        return clean

    if full_name:
        tokens = [
            re.sub(r"[^A-Za-z0-9]", "", strip_accents(tok))
            for tok in full_name.strip().split()
        ]
        tokens = [t for t in tokens if t]
        if not tokens:
            raise ValueError("El nombre completo no contiene caracteres válidos.")
        if len(tokens) == 1:
            return tokens[0].capitalize()
        first_initial = tokens[0][0].upper()
        last_name = tokens[1][0].upper() + tokens[1][1:]
        return f"{first_initial}{last_name}"

    raise ValueError("Debes proporcionar --acronym o --full-name.")


def next_sequence_number(existing_names: list[str]) -> int:
    max_num = 0
    for name in existing_names:
        m = FOLDER_PATTERN.match(name)
        if m:
            num = int(m.group(1))
            if num > max_num:
                max_num = num
    return max_num + 1


def run_cmd(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"Error ejecutando {' '.join(cmd)} (code {proc.returncode}):\n{proc.stderr.strip()}"
        )
    return proc.stdout


def parse_mkdir_id(output: str) -> str:
    m = re.search(r"ID:\s*([A-Za-z0-9_-]+)", output)
    if not m:
        raise RuntimeError(f"No se pudo extraer el ID de la salida de gdrive mkdir: {output}")
    return m.group(1)


def create_in_drive(parent_id: str, acronym: str, dry_run: bool = False) -> dict:
    raw = run_cmd(["gdrive", "readonly", "ls", parent_id, "--json"])
    items = json.loads(raw) if raw.strip() else []
    existing_names = [
        item.get("name", "")
        for item in items
        if item.get("mimeType") == "application/vnd.google-apps.folder"
    ]
    seq = next_sequence_number(existing_names)
    folder_name = f"{seq:03d}_Tesis_Antigravity_{acronym}"

    if dry_run:
        return {
            "mode": "drive",
            "dry_run": True,
            "parent_id": parent_id,
            "sequence": f"{seq:03d}",
            "folder_name": folder_name,
            "subfolders": SUBFOLDERS,
        }

    out = run_cmd(["gdrive", "mutate", "mkdir", folder_name, "--parent", parent_id])
    folder_id = parse_mkdir_id(out)

    created_subfolders = {}
    for sub in SUBFOLDERS:
        sub_out = run_cmd(["gdrive", "mutate", "mkdir", sub, "--parent", folder_id])
        sub_id = parse_mkdir_id(sub_out)
        created_subfolders[sub] = {
            "id": sub_id,
            "url": f"https://drive.google.com/drive/folders/{sub_id}",
        }

    return {
        "mode": "drive",
        "parent_id": parent_id,
        "sequence": f"{seq:03d}",
        "folder_name": folder_name,
        "folder_id": folder_id,
        "url": f"https://drive.google.com/drive/folders/{folder_id}",
        "subfolders": created_subfolders,
    }


def create_locally(base_dir: str, acronym: str, dry_run: bool = False) -> dict:
    root = Path(base_dir).expanduser().resolve()
    existing_names = []
    if root.exists():
        existing_names = [p.name for p in root.iterdir() if p.is_dir()]
    seq = next_sequence_number(existing_names)
    folder_name = f"{seq:03d}_Tesis_Antigravity_{acronym}"
    project_path = root / folder_name

    if dry_run:
        return {
            "mode": "local",
            "dry_run": True,
            "base_dir": str(root),
            "sequence": f"{seq:03d}",
            "folder_name": folder_name,
            "path": str(project_path),
            "subfolders": SUBFOLDERS,
        }

    project_path.mkdir(parents=True, exist_ok=True)
    created_subfolders = {}
    for sub in SUBFOLDERS:
        sub_path = project_path / sub
        sub_path.mkdir(parents=True, exist_ok=True)
        created_subfolders[sub] = {"path": str(sub_path)}

    return {
        "mode": "local",
        "base_dir": str(root),
        "sequence": f"{seq:03d}",
        "folder_name": folder_name,
        "path": str(project_path),
        "subfolders": created_subfolders,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Crea carpeta correlativa 000_Tesis_Antigravity_<Acronimo> en local o Google Drive."
    )
    parser.add_argument("--acronym", help="Acrónimo de apellido (ej. EHuayna).")
    parser.add_argument(
        "--full-name",
        help="Nombre y apellido completo del tesista para generar el acrónimo automáticamente.",
    )
    parser.add_argument(
        "--parent-id",
        default=DEFAULT_DRIVE_OUTPUT_FOLDER_ID,
        help="ID de la carpeta padre en Google Drive (o usa TESIS_DRIVE_OUTPUT_FOLDER_ID).",
    )
    parser.add_argument(
        "--local-dir",
        help="Directorio local donde crear el proyecto (default: ./tesis_output si no se usa Drive).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Solo calcula y muestra el nombre correlativo sin crear carpetas.",
    )
    args = parser.parse_args()

    try:
        acronym = normalize_acronym(args.acronym, args.full_name)
        if args.local_dir or not args.parent_id:
            target_dir = args.local_dir or "./tesis_output"
            result = create_locally(target_dir, acronym, dry_run=args.dry_run)
        else:
            result = create_in_drive(args.parent_id, acronym, dry_run=args.dry_run)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
