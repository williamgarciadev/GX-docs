#!/usr/bin/env python3
"""
Genera corpus_bantotal/ (grounding Bantotal) a partir de las fuentes en
bantotal_sources/:

  - MDU-99000-GL-V3R1.11.pdf          : manual oficial (FUENTE PRIMARIA,
                                         licencia internal-use, no se parsea
                                         aqui; se cita como referencia).
  - Analisis_Modelo_Datos_Bantotal.md : analisis tecnico derivado (80 tablas,
                                         118 paginas). Fuente de tables.tsv.
  - Patron_9_Campos_Bantotal.md       : patron arquitectonico de 9 campos.
                                         Fuente de nine_fields.md.

Salidas:
  - corpus_bantotal/tables.tsv    : catalogo code\tname\tfamily\tnote\tsource
  - corpus_bantotal/families.tsv  : prefijo\tcategoria\tproposito
  - corpus_bantotal/nine_fields.md: copia curada del patron de 9 campos

IMPORTANTE (verificacion): tables.tsv se deriva de un ANALISIS SECUNDARIO del
manual, no de una extraccion literal del PDF pagina por pagina. Es una buena
guia de que tablas EXISTEN y su proposito, pero para la estructura EXACTA de
campos de una tabla especifica hay que confirmar contra el PDF
`bantotal_sources/MDU-99000-GL-V3R1.11.pdf` (o la skill bantotal-table-extractor).

Idempotente: re-ejecutarlo reconstruye corpus_bantotal/{tables,families}.tsv y
nine_fields.md. No toca xpz_objects.tsv (ese lo genera scan_bantotal_xpz.py a
partir de .xpz reales que el usuario agregue).
"""
import os
import re

SRC_DIR = "bantotal_sources"
ANALYSIS_MD = os.path.join(SRC_DIR, "Analisis_Modelo_Datos_Bantotal.md")
NINE_FIELDS_MD = os.path.join(SRC_DIR, "Patron_9_Campos_Bantotal.md")
OUT_DIR = "corpus_bantotal"

TABLE_ROW_RE = re.compile(
    r"^\|\s*\*\*([A-Z]{2,4}[0-9]{3})\*\*\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
)

# Categorias de prefijo de tabla documentadas en la seccion
# "Sistema de Nomenclatura / Clasificacion de Tablas por Prefijo" del analisis.
FAMILIES = [
    ("FST", "Tablas Basicas", "Parametros y configuraciones del sistema"),
    ("FSD", "Datos", "Informacion transaccional y operativa"),
    ("FSR", "Relaciones", "Vinculos y asociaciones entre entidades"),
    ("FSE", "Extensiones", "Datos adicionales y especializados"),
    ("FSH", "Historicos", "Registros de auditoria y cambios"),
    ("FSX", "Textos", "Descripciones y comentarios"),
    ("FSA", "Auxiliares", "Tablas de apoyo y temporales"),
    ("FSI", "Informaciones", "Reportes y vistas de consulta"),
    ("FSM", "Menues", "Interfaces de usuario y navegacion"),
    ("FSN", "Numeradores", "Secuencias automaticas y contadores"),
]


def family_for(code):
    for prefix, _cat, _purpose in FAMILIES:
        if code.startswith(prefix):
            return prefix
    return code[:3]


def build_tables_tsv():
    rows = {}
    with open(ANALYSIS_MD, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            m = TABLE_ROW_RE.match(line)
            if not m:
                continue
            code, name, note = m.group(1), m.group(2).strip(), m.group(3).strip()
            if code in rows:
                continue  # primera aparicion gana (mas cerca del catalogo canonico)
            rows[code] = (name, family_for(code), note, lineno)

    out_path = os.path.join(OUT_DIR, "tables.tsv")
    with open(out_path, "w", encoding="utf-8") as f:
        for code in sorted(rows):
            name, family, note, lineno = rows[code]
            source = f"{ANALYSIS_MD}:L{lineno}"
            f.write(f"{code}\t{name}\t{family}\t{note}\t{source}\n")
    return len(rows)


def build_families_tsv():
    out_path = os.path.join(OUT_DIR, "families.tsv")
    with open(out_path, "w", encoding="utf-8") as f:
        for prefix, cat, purpose in FAMILIES:
            f.write(f"{prefix}\t{cat}\t{purpose}\n")
    return len(FAMILIES)


def build_nine_fields():
    with open(NINE_FIELDS_MD, encoding="utf-8") as f:
        content = f.read()
    header = (
        "<!-- Generado por build_bantotal_corpus.py a partir de "
        f"{NINE_FIELDS_MD}. No editar a mano; editar la fuente y "
        "reconstruir. -->\n\n"
    )
    out_path = os.path.join(OUT_DIR, "nine_fields.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + content)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(os.path.join(OUT_DIR, "bantotal_xpz"), exist_ok=True)
    n_tables = build_tables_tsv()
    n_fam = build_families_tsv()
    build_nine_fields()
    xpz_path = os.path.join(OUT_DIR, "xpz_objects.tsv")
    if not os.path.exists(xpz_path):
        with open(xpz_path, "w", encoding="utf-8") as f:
            pass  # lo puebla scan_bantotal_xpz.py cuando haya .xpz reales
    print(f"tables.tsv: {n_tables} tablas")
    print(f"families.tsv: {n_fam} familias")
    print("nine_fields.md generado")
    print(f"xpz_objects.tsv: {'existente' if os.path.getsize(xpz_path) else 'vacio (sin .xpz aun)'}")


if __name__ == "__main__":
    main()
