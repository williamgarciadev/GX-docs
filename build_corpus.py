#!/usr/bin/env python3
"""
Transforma genexus_documentation.md (volcado de wiki.genexus.com) en un corpus
"grounding-ready" para agentes IA:

  - corpus/articles/<id>-<slug>.md  : un archivo por articulo, con frontmatter
                                       (title, source_id, source_url, genexus_version)
  - corpus/genexus_corpus.jsonl     : un registro JSON por articulo
  - corpus/INDEX.md                 : indice navegable con enlaces y procedencia

Limpieza aplicada por articulo:
  - elimina el titulo H1 duplicado y el bloque "File:/Newest Version"
  - reescribe enlaces internos NNNN.html -> https://wiki.genexus.com/commwiki/wiki?NNNN
  - conserva la URL de origen como procedencia verificable
"""
import json
import os
import re
import sys

SRC = "genexus_documentation.md"
OUT = "corpus"
WIKI = "https://wiki.genexus.com/commwiki/wiki?{}"
GX_VERSION = "18"

file_re = re.compile(r"^File:\s+(\d+)\.html\s*$")
h1_re = re.compile(r"^# (.+?)\s*$")
# enlaces tipo ](1964.html) o ](1964.html#anchor)
link_re = re.compile(r"\]\((\d+)\.html(#[^)]*)?\)")
# imagenes rotas: ![alt](./images/NNNN.ext) -> no se subieron las imagenes
img_re = re.compile(
    r"!\[[^\]]*\]\(\./images/(\d+)\.(?:png|jpe?g|gif|bmp|svg)\)", re.IGNORECASE
)
# bloque mini-tabla "Newest Version"
newest_block_re = re.compile(
    r"\n?\|\s*\|\n\| --- \|\n\| \[Newest Version\][^\n]*\n", re.MULTILINE
)
# Escaneo de metodos documentados DENTRO de articulos: se capturan los nombres
# que aparecen a la vez como encabezado "#### [Nombre]" y como llamada
# ".Nombre(" en el mismo articulo (doble senal = alta precision; descarta
# encabezados de seccion y llamadas sueltas de ejemplo).
head_method_re = re.compile(r"^#{3,4}\s*\[?\*{0,2}([A-Z][A-Za-z0-9]{2,})\*{0,2}\]?", re.M)
call_method_re = re.compile(r"\.([A-Z][A-Za-z0-9]{2,})\s*\(")
# Sintaxis de funcion documentada: nombre en negrita pegado al "(" (p. ej.
# "**StrSearch(**" o "**Substr(***"). El "(" debe ir SIN espacio para no
# capturar celdas de tabla como "**Character (n)**". Se exige ademas que el
# articulo tenga "Type Returned" (marca de funcion/metodo).
syntax_func_re = re.compile(r"\*\*([A-Z][A-Za-z0-9_]{2,})\(")
# Propiedades documentadas DENTRO de articulos compuestos: el autor las etiqueta
# explicitamente con "property"/"properties" como texto de enlace cruzado
# "[Nombre property](url-wiki)" o como celda de tabla "| Nombre property |".
# Doble senal (nombre + etiqueta "property" en contexto estructurado, no prosa
# libre) = alta precision. El enlace se ejecuta tras reescribir las URLs, por eso
# se exige dominio absoluto wiki.genexus.com.
prop_link_re = re.compile(
    r"\[([A-Z][A-Za-z0-9][A-Za-z0-9 _/-]*?) [Pp]ropert(?:y|ies)\]"
    r"\((https://wiki\.genexus\.com[^)]*)\)"
)
prop_cell_re = re.compile(
    r"\|\s*\*{0,2}([A-Z][A-Za-z0-9][A-Za-z0-9 _/-]*?) [Pp]ropert(?:y|ies)\*{0,2}\s*\|"
)
PROP_STOP = {"all", "advanced", "general", "basic", "other", "others", "none"}
LITERAL_STOP = {
    "true", "false", "null", "and", "or", "not", "if", "then", "else",
    "while", "for", "each", "do", "case", "when", "sub", "new", "return",
    "exit", "where", "endif", "endfor", "endsub", "endcase",
}
SECTION_HEADINGS = {
    "syntax", "example", "examples", "description", "scope", "overview",
    "remarks", "note", "notes", "see", "parameters", "return", "returns",
    "features", "properties", "methods", "definition", "introduction",
    "sample", "samples", "usage", "values", "purpose", "considerations",
    "availability", "object", "objects", "output", "input",
}


def slugify(text, maxlen=60):
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rstrip("-")
    return s or "untitled"


def rewrite_links(text):
    return link_re.sub(
        lambda m: "](" + WIKI.format(m.group(1)) + (m.group(2) or "") + ")", text
    )


def main():
    with open(SRC, encoding="utf-8") as f:
        lines = f.read().split("\n")

    # localizar inicios de articulo: linea "File: NNNN.html" precedida por su titulo H1
    markers = []  # (title_line_idx, file_line_idx, id)
    for i, line in enumerate(lines):
        m = file_re.match(line)
        if not m:
            continue
        # titulo = primer H1 hacia atras
        t = i - 1
        while t >= 0 and not h1_re.match(lines[t]):
            t -= 1
        if t < 0:
            continue
        markers.append((t, i, m.group(1)))

    print(f"Articulos detectados: {len(markers)}")

    os.makedirs(os.path.join(OUT, "articles"), exist_ok=True)
    jsonl_path = os.path.join(OUT, "genexus_corpus.jsonl")
    seen_ids = {}
    index_rows = []
    n_links = 0
    scanned_methods = {}     # name -> url (metodos: encabezado ∩ llamada)
    syntax_funcs = {}        # name -> url (sintaxis "**Name(" + Type Returned)
    method_called_all = set()  # nombres invocados como ".Name(" en todo el corpus
    scanned_props = {}       # key(lower) -> (name, url) propiedades del cuerpo

    with open(jsonl_path, "w", encoding="utf-8") as jf:
        for k, (t_idx, f_idx, art_id) in enumerate(markers):
            end = markers[k + 1][0] if k + 1 < len(markers) else len(lines)
            title = h1_re.match(lines[t_idx]).group(1).strip()

            # cuerpo = desde despues del titulo hasta el siguiente articulo
            body_lines = lines[t_idx + 1 : end]
            body = "\n".join(body_lines)

            # quitar linea "File: NNNN.html"
            body = re.sub(r"^File:\s+\d+\.html\s*$", "", body, flags=re.MULTILINE)
            # quitar bloque "Newest Version"
            body = newest_block_re.sub("\n", body)
            # quitar el titulo H1 duplicado (primera aparicion exacta)
            dup = re.compile(r"^# " + re.escape(title) + r"\s*$", re.MULTILINE)
            body = dup.sub("", body, count=1)
            # reescribir enlaces internos
            n_links += len(link_re.findall(body))
            body = rewrite_links(body)
            # imagenes no incluidas: marcador neutro (evita rutas rotas)
            body = img_re.sub(r"`[imagen omitida: wiki id \1]`", body)
            # normalizar lineas en blanco y separadores sobrantes
            body = re.sub(r"\n{3,}", "\n\n", body).strip()
            body = re.sub(r"^---\s*$", "", body, count=1, flags=re.MULTILINE).strip()

            source_url = WIKI.format(art_id)

            # metodos documentados dentro del articulo (encabezado ∩ llamada)
            heads = {h for h in head_method_re.findall(body)
                     if h.lower() not in SECTION_HEADINGS}
            calls = set(call_method_re.findall(body))
            method_called_all |= calls
            for mname in heads & calls:
                scanned_methods.setdefault(mname, source_url)
            # funciones documentadas por bloque de sintaxis ("**Name(" + Type Returned)
            if "Type Returned" in body or "Type returned" in body:
                for fname in syntax_func_re.findall(body):
                    if fname.lower() not in LITERAL_STOP:
                        syntax_funcs.setdefault(fname, source_url)
            # propiedades etiquetadas dentro del articulo (enlace cruzado / celda)
            for pm in prop_link_re.finditer(body):
                pname, purl = pm.group(1).strip(), pm.group(2)
                key = pname.lower()
                if (key not in PROP_STOP and 2 <= len(pname) <= 40
                        and len(pname.split()) <= 4):
                    scanned_props.setdefault(key, (pname, purl))
            for pm in prop_cell_re.finditer(body):
                pname = pm.group(1).strip()
                key = pname.lower()
                if (key not in PROP_STOP and 2 <= len(pname) <= 40
                        and len(pname.split()) <= 4):
                    scanned_props.setdefault(key, (pname, source_url))

            slug = slugify(title)
            uid = art_id
            if uid in seen_ids:
                seen_ids[uid] += 1
                fname = f"{art_id}-{slug}-{seen_ids[uid]}.md"
            else:
                seen_ids[uid] = 0
                fname = f"{art_id}-{slug}.md"
            rel = os.path.join("articles", fname)

            frontmatter = (
                "---\n"
                f"title: {json.dumps(title, ensure_ascii=False)}\n"
                f"source_id: {art_id}\n"
                f"source_url: {source_url}\n"
                f"genexus_version: \"{GX_VERSION}\"\n"
                "---\n\n"
            )
            with open(os.path.join(OUT, rel), "w", encoding="utf-8") as af:
                af.write(frontmatter + f"# {title}\n\n" + body + "\n")

            jf.write(
                json.dumps(
                    {
                        "id": art_id,
                        "title": title,
                        "source_url": source_url,
                        "genexus_version": GX_VERSION,
                        "path": rel,
                        "content": body,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
            index_rows.append((art_id, title, rel, source_url))

    # indice navegable
    with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8") as ix:
        ix.write("# Indice del corpus GeneXus\n\n")
        ix.write(f"{len(index_rows)} articulos. Fuente: wiki.genexus.com (GeneXus 18).\n\n")
        ix.write("| ID | Articulo | Fuente |\n|----|----------|--------|\n")
        for art_id, title, rel, url in sorted(index_rows, key=lambda r: int(r[0])):
            safe = title.replace("|", "\\|")
            ix.write(f"| {art_id} | [{safe}]({rel}) | [wiki]({url}) |\n")

    # indice plano para busqueda rapida (lo usa el hook de grounding)
    with open(os.path.join(OUT, "index.tsv"), "w", encoding="utf-8") as tv:
        for art_id, title, rel, url in sorted(index_rows, key=lambda r: int(r[0])):
            tv.write(f"{art_id}\t{title}\t{rel}\t{url}\n")

    # catalogo de API verificada (funciones/metodos/comandos) extraida de los
    # titulos "<Nombre> function|method|command". Lo usa el hook para que el
    # agente no invente nombres que GeneXus no tiene.
    KIND = {
        "function": "function", "functions": "function",
        "method": "method", "methods": "method",
        "command": "command", "commands": "command",
    }
    ident = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
    skip = re.compile(r"^(howto|how to|example|tutorial|sample)\b", re.IGNORECASE)
    api = {}  # (name, kind) -> url
    for art_id, title, rel, url in index_rows:
        if skip.match(title) or "deploy" in title.lower():
            continue
        words = title.split()
        if not words:
            continue
        kind = KIND.get(words[-1].lower())
        if not kind:
            continue
        namepart = " ".join(words[:-1]).rstrip(" -–")
        for cand in re.split(r",| and ", namepart):
            cand = cand.strip()
            if ident.match(cand):
                api.setdefault((cand, kind), url)
    # API verificada documentada DENTRO de articulos compuestos (no como
    # titulo "<Nombre> method"), por eso la extraccion por titulo no la captura.
    # Sembrada a mano con su source_url verificado.
    EXTRA_API = [
        ("IsMatch", "method", WIKI.format(4606)),       # RegEx (RegEx)
        ("ReplaceRegEx", "method", WIKI.format(4606)),  # RegEx (RegEx)
    ]
    for name, kind, url in EXTRA_API:
        api.setdefault((name, kind), url)
    # metodos auto-capturados del cuerpo de los articulos (no pisan los ya
    # presentes como funcion/comando/metodo por titulo).
    in_api = lambda nm: any((nm, k) in api for k in ("function", "method", "command"))
    n_scanned_new = 0
    for name, url in scanned_methods.items():
        if not in_api(name):
            api[(name, "method")] = url
            n_scanned_new += 1
    # funciones por sintaxis: el tipo se decide a nivel de corpus (si se invoca
    # como ".Name(" en algun sitio es metodo; si no, funcion).
    n_syntax_new = 0
    for name, url in syntax_funcs.items():
        if not in_api(name):
            kind = "method" if name in method_called_all else "function"
            api[(name, kind)] = url
            n_syntax_new += 1
    with open(os.path.join(OUT, "api.tsv"), "w", encoding="utf-8") as af:
        for (name, kind), url in sorted(api.items(), key=lambda x: (x[0][1], x[0][0].lower())):
            af.write(f"{name}\t{kind}\t{url}\n")
    n_api = len(api)

    # catalogo de propiedades verificadas. Los nombres suelen ser multipalabra
    # (p. ej. "Maximum length"), por eso se permiten espacios.
    prop_name = re.compile(r"^[A-Za-z][A-Za-z0-9 _/-]*$")
    props = {}  # name -> url
    for art_id, title, rel, url in index_rows:
        if skip.match(title):
            continue
        words = title.split()
        if not words or words[-1].lower() not in ("property", "properties"):
            continue
        name = " ".join(words[:-1]).strip(" -–")
        if len(name) >= 2 and prop_name.match(name):
            props.setdefault(name, url)
    # propiedades auto-capturadas del cuerpo de articulos compuestos (no pisan
    # las ya presentes por titulo; dedup case-insensitive).
    titled_lower = {k.lower() for k in props}
    n_props_scanned = 0
    for key, (pname, purl) in scanned_props.items():
        if key not in titled_lower and prop_name.match(pname):
            props[pname] = purl
            titled_lower.add(key)
            n_props_scanned += 1
    with open(os.path.join(OUT, "properties.tsv"), "w", encoding="utf-8") as pf:
        for name, url in sorted(props.items(), key=lambda x: x[0].lower()):
            pf.write(f"{name}\t{url}\n")
    n_props = len(props)

    # catalogo de eventos verificados (titulos "<Nombre> event").
    events = {}  # name -> url
    for art_id, title, rel, url in index_rows:
        if skip.match(title):
            continue
        words = title.split()
        if not words or words[-1].lower() not in ("event", "events"):
            continue
        name = " ".join(words[:-1]).strip(" -–")
        # nombres reales de eventos son cortos; frases largas son ruido
        # (p. ej. paginas de categoria "Maps Control Type Events").
        if len(name) >= 2 and len(name.split()) <= 3 and prop_name.match(name):
            events.setdefault(name, url)
    with open(os.path.join(OUT, "events.tsv"), "w", encoding="utf-8") as ef:
        for name, url in sorted(events.items(), key=lambda x: x[0].lower()):
            ef.write(f"{name}\t{url}\n")
    n_events = len(events)

    # catalogo de Data Types verificados (titulos "<Nombre> data type(s)").
    datatypes = {}  # name -> url
    for art_id, title, rel, url in index_rows:
        if skip.match(title):
            continue
        words = title.split()
        if len(words) < 3 or [w.lower() for w in words[-2:]] not in (
            ["data", "type"], ["data", "types"]
        ):
            continue
        name = " ".join(words[:-2]).strip(" -–")
        # nombres reales de Data Types son cortos; frases largas son ruido
        # (p. ej. "Save Method for ... extended Data Types").
        if len(name) >= 2 and len(name.split()) <= 3 and prop_name.match(name):
            datatypes.setdefault(name, url)
    with open(os.path.join(OUT, "datatypes.tsv"), "w", encoding="utf-8") as df_:
        for name, url in sorted(datatypes.items(), key=lambda x: x[0].lower()):
            df_.write(f"{name}\t{url}\n")
    n_dts = len(datatypes)

    print(f"Enlaces internos reescritos: {n_links}")
    print(f"Escritos {len(index_rows)} .md en {OUT}/articles/")
    print(f"JSONL: {jsonl_path}")
    print(f"Indice: {OUT}/INDEX.md  +  {OUT}/index.tsv")
    print(f"Catalogo API verificada: {OUT}/api.tsv ({n_api} nombres; "
          f"+{n_scanned_new} metodos, +{n_syntax_new} por sintaxis, del cuerpo)")
    print(f"Catalogo propiedades: {OUT}/properties.tsv ({n_props} nombres; "
          f"+{n_props_scanned} del cuerpo)")
    print(f"Catalogo eventos: {OUT}/events.tsv ({n_events} nombres)")
    print(f"Catalogo Data Types: {OUT}/datatypes.tsv ({n_dts} nombres)")


if __name__ == "__main__":
    main()
