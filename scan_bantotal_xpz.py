#!/usr/bin/env python3
"""
Escanea corpus_bantotal/bantotal_xpz/*.xpz (exports de GeneXus de tu KB
Bantotal) y regenera corpus_bantotal/xpz_objects.tsv: un catalogo verificado
de los objetos, atributos y variables que REALMENTE existen en tu KB, para
usar como grounding ademas de tables.tsv (que sale del manual generico).

Uso:
    python3 scan_bantotal_xpz.py

No hace falta ningun paso previo: si corpus_bantotal/bantotal_xpz/ esta vacio
(caso por defecto de este repo), simplemente deja xpz_objects.tsv vacio.
Agrega tus .xpz a esa carpeta y vuelve a correr este script para poblarlo.

Columnas de xpz_objects.tsv: name\ttype\tmodule\tattributes_or_vars\tsource_xpz
  - "type": Transaction | Procedure | SDT | WebPanel | WorkPanel | DataProvider | ...
  - "attributes_or_vars": primeros nombres de atributos/variables (para
    verificar existencia de un campo sin abrir el .xpz), separados por ";"
  - "source_xpz": archivo .xpz de origen (procedencia)

Idempotente: solo lee corpus_bantotal/bantotal_xpz/*.xpz, no requiere red ni
dependencias externas (solo stdlib).
"""
import os
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

OUT_DIR = "corpus_bantotal"
XPZ_DIR = os.path.join(OUT_DIR, "bantotal_xpz")
OUT_TSV = os.path.join(OUT_DIR, "xpz_objects.tsv")

OBJECT_TYPES = {
    "2a9e9aba-d2de-4801-ae7f-5e3819222daf": "Transaction",
    "1db606f2-af09-4cf9-a3b5-b481519d28f6": "Transaction",
    "84a12160-f59b-4ad7-a683-ea4481ac23e9": "Procedure",
    "447527b5-9210-4523-898b-5dccb17be60a": "SDT",
    "c88fffcd-b6f8-0000-8fec-00b5497e2117": "DataView",
    "857ca50e-7905-0000-0007-c5d9ff2975ec": "DataView",
    "00000000-0000-0000-0000-000000000001": "WorkPanel",
    "19abc6ff-2cd2-0000-0006-6d172bc2333b": "WorkPanel",
    "ba6a82ac-a9f0-4b8b-a4c4-f42e5c45e4e0": "WebPanel",
    "c9584656-94b6-4ccd-890f-332d11fc2c25": "WebPanel",
    "5a3ecddd-f78d-4d02-8b29-d33abd78c0b4": "DataProvider",
    "9a8bd941-4e51-4e85-9db2-a43cf0f0f4b3": "DataSelector",
    "00972a17-9975-449e-aab1-d26165d51393": "Enum_Domain",
    "c804fdbd-7c0b-440d-8527-4316c92649a6": "Module",
    "fc1b76c4-95c5-0000-0101-44f9543121bd": "ExternalObject",
    "00000000-0000-0000-0000-000000000006": "Folder",
    "00000000-0000-0000-0000-000000000008": "Folder",
}

PART_TYPES = {
    "264be5fb-1b28-4b25-a598-6ca900dd059f": "Transaction_Structure",
    "e4c4ade7-53f0-4a56-bdfd-843735b66f47": "Variables",
    "5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a": "SDT_Structure",
}


def resolve_type(type_guid):
    return OBJECT_TYPES.get(type_guid.lower().strip("{}"), "Unknown")


def load_xpz(path):
    try:
        with zipfile.ZipFile(path, "r") as zf:
            xml_files = [f for f in zf.namelist() if f.endswith(".xml")]
            if not xml_files:
                raise ValueError("sin XML dentro del xpz")
            content = zf.read(xml_files[0])
    except zipfile.BadZipFile:
        with open(path, "rb") as f:
            content = f.read()
    if content.startswith(b"\xef\xbb\xbf"):
        content = content[3:]
    return ET.fromstring(content)


def collect_attr_names(level_elem, out):
    for child in level_elem:
        if child.tag == "Attribute":
            name = child.text or child.get("name", "")
            if name:
                out.append(name)
        elif child.tag == "Level":
            collect_attr_names(child, out)


def collect_sdt_item_names(level_elem, out):
    for child in level_elem:
        if child.tag == "Item":
            name = child.get("name", "")
            if name:
                out.append(name)
        elif child.tag == "Level":
            collect_sdt_item_names(child, out)


def parse_object(obj_elem, xpz_name):
    type_guid = obj_elem.get("type", "")
    type_name = resolve_type(type_guid)
    if type_name == "Folder":
        return None
    name = obj_elem.get("name", "")
    module = obj_elem.get("parent", "") or "-"

    fields = []
    for part in obj_elem.findall("Part"):
        part_type = PART_TYPES.get(part.get("type", ""), "")
        if part_type == "Transaction_Structure":
            for level in part.findall("Level"):
                collect_attr_names(level, fields)
        elif part_type == "SDT_Structure":
            for level in part.findall("Level"):
                collect_sdt_item_names(level, fields)
        elif part_type == "Variables":
            for var in part.findall(".//Variable"):
                vname = var.get("Name", "")
                if vname:
                    fields.append(vname)

    return name, type_name, module, fields, xpz_name


def scan_file(path):
    root = load_xpz(path)
    objs_elem = root.find("Objects")
    if objs_elem is None:
        return []
    results = []
    for obj_elem in objs_elem.findall("Object"):
        r = parse_object(obj_elem, os.path.basename(path))
        if r and r[0]:
            results.append(r)
    return results


def main():
    os.makedirs(XPZ_DIR, exist_ok=True)
    xpz_files = sorted(Path(XPZ_DIR).glob("*.xpz"))

    rows = []
    for path in xpz_files:
        try:
            rows.extend(scan_file(str(path)))
        except Exception as e:  # noqa: BLE001 - reportar y seguir con el resto
            print(f"aviso: no se pudo parsear {path.name}: {e}", file=sys.stderr)

    with open(OUT_TSV, "w", encoding="utf-8") as f:
        for name, type_name, module, fields, xpz_name in sorted(rows, key=lambda r: (r[1], r[0])):
            field_list = ";".join(fields[:25])
            f.write(f"{name}\t{type_name}\t{module}\t{field_list}\t{xpz_name}\n")

    if not xpz_files:
        print(f"Sin .xpz en {XPZ_DIR}/. xpz_objects.tsv queda vacio.")
        print("Agrega tus exports de GeneXus (.xpz) ahi y vuelve a correr este script.")
    else:
        print(f"{len(rows)} objetos catalogados desde {len(xpz_files)} archivo(s) .xpz -> {OUT_TSV}")


if __name__ == "__main__":
    main()
