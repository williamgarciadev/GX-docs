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

    print(f"Enlaces internos reescritos: {n_links}")
    print(f"Escritos {len(index_rows)} .md en {OUT}/articles/")
    print(f"JSONL: {jsonl_path}")
    print(f"Indice: {OUT}/INDEX.md  +  {OUT}/index.tsv")


if __name__ == "__main__":
    main()
