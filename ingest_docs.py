#!/usr/bin/env python3
"""
Ingesta generica de documentos .md/.html sueltos hacia el corpus GeneXus o
Bantotal, para sumarlos como articulos citables (busqueda + grounding) sin
tener que tocar build_corpus.py / build_bantotal_corpus.py.

Carpetas "drop-in" (dejas tus archivos ahi):
    extra_docs/genexus/*.{md,html}
    extra_docs/bantotal/*.{md,html}

Que hace por cada archivo:
    1. Si es .html, lo convierte a texto/markdown simple (sin dependencias
       externas: usa html.parser de la stdlib).
    2. Extrae titulo (primer H1/<h1>, o el nombre de archivo si no hay).
    3. Si el documento tiene 2+ encabezados `## ` (tipo "chuleta" con varias
       secciones bajo un titulo generico), lo PARTE en un articulo por
       seccion (titulo = "<titulo doc> — <encabezado seccion>") mas un
       articulo de intro si hay contenido antes de la primera seccion. Sin
       esto, un documento largo con muchos temas quedaria casi invisible
       para consultas puntuales: el hook de grounding rankea articulos por
       coincidencia de TITULO, no de cuerpo completo.
    4. Le asigna un id sintetico >= 9000001 por cada articulo generado (los
       ids de wiki de GeneXus llegan a ~61122; Bantotal no usa ids numericos
       hoy) para que nunca choque con un id real.
    5. Escribe el articulo en corpus/articles/ o corpus_bantotal/articles/ con
       frontmatter, marcando `source_url: local:extra_docs/<target>/<archivo>`
       -- NO es una URL de wiki.genexus.com; es tu documento, no lo cites como
       si fuera oficial.
    6. Reconstruye el `index.tsv` correspondiente: conserva las filas
       existentes (wiki/derivadas) y reemplaza solo el bloque de articulos
       "extra" (ids >= 9000001) con el resultado de esta corrida.

Idempotente: correr sin cambios en extra_docs/ dos veces da el mismo
resultado; si borras un archivo de extra_docs/, su articulo generado
desaparece en la siguiente corrida.

Uso:
    python3 ingest_docs.py            # procesa ambos targets
    python3 ingest_docs.py genexus    # solo GeneXus
    python3 ingest_docs.py bantotal   # solo Bantotal
"""
import glob
import os
import re
import sys
import unicodedata
from html.parser import HTMLParser

BASE_ID = 9_000_001

TARGETS = {
    "genexus": {
        "src_dir": os.path.join("extra_docs", "genexus"),
        "out_dir": os.path.join("corpus", "articles"),
        "index_path": os.path.join("corpus", "index.tsv"),
        "extra_note": "genexus_version: \"18\"\n",
    },
    "bantotal": {
        "src_dir": os.path.join("extra_docs", "bantotal"),
        "out_dir": os.path.join("corpus_bantotal", "articles"),
        "index_path": os.path.join("corpus_bantotal", "index.tsv"),
        "extra_note": "",
    },
}


def slugify(text, maxlen=60):
    # normaliza tildes/enies (comunes en documentos en espanol, a diferencia
    # de los titulos del wiki de GeneXus, casi todos en ingles) antes de
    # descartar todo lo que no sea [a-z0-9], para no perder letras completas.
    s = unicodedata.normalize("NFD", text.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rstrip("-")
    return s or "untitled"


class _HTMLToText(HTMLParser):
    """Conversor HTML -> texto/markdown minimo, sin dependencias externas.
    No pretende ser exhaustivo: cubre lo suficiente (encabezados, parrafos,
    listas, enlaces, negrita/codigo) para que un documento HTML razonable
    quede legible y buscable como markdown."""

    BLOCK_TAGS = {"p", "div", "section", "article", "tr", "table"}
    HEADING_TAGS = {"h1": "#", "h2": "##", "h3": "###", "h4": "####",
                    "h5": "#####", "h6": "######"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip_depth = 0
        self.link_href = None

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip_depth += 1
            return
        if tag in self.HEADING_TAGS:
            self.out.append(f"\n\n{self.HEADING_TAGS[tag]} ")
        elif tag in self.BLOCK_TAGS or tag == "br":
            self.out.append("\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("_")
        elif tag in ("code", "pre"):
            self.out.append("`")
        elif tag == "a":
            self.link_href = dict(attrs).get("href")
            self.out.append("[")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if tag in self.HEADING_TAGS or tag in self.BLOCK_TAGS:
            self.out.append("\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("_")
        elif tag in ("code", "pre"):
            self.out.append("`")
        elif tag == "a":
            href = self.link_href or ""
            self.out.append(f"]({href})")
            self.link_href = None

    def handle_data(self, data):
        if self.skip_depth:
            return
        self.out.append(data)

    def text(self):
        raw = "".join(self.out)
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


def html_to_text(html):
    p = _HTMLToText()
    p.feed(html)
    return p.text()


def extract_title(text, fallback):
    m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fallback


H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
MIN_SECTIONS_TO_SPLIT = 2


def split_sections(body):
    """Si el documento tiene >= MIN_SECTIONS_TO_SPLIT encabezados H2, lo parte
    en (intro, [(heading, section_body), ...]) para que cada seccion se pueda
    ingerir como articulo propio (titulo especifico -> mejor recall en el
    ranking por titulo del hook de grounding, que no mira el cuerpo). Un
    documento tipo "chuleta" con 30 secciones bajo un solo titulo generico
    quedaria casi invisible para consultas puntuales si no se parte asi.
    Si hay menos de 2 H2, devuelve (body, []) sin partir."""
    matches = list(H2_RE.finditer(body))
    if len(matches) < MIN_SECTIONS_TO_SPLIT:
        return body, []
    intro = body[: matches[0].start()].strip()
    sections = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        heading = m.group(1).strip()
        sections.append((heading, body[start:end].strip()))
    return intro, sections


def load_index(path):
    rows = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) == 4:
                    rows.append(parts)
    except OSError:
        pass
    return rows


def ingest_target(name, cfg):
    src_dir, out_dir, index_path = cfg["src_dir"], cfg["out_dir"], cfg["index_path"]
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    # limpiar articulos "extra" de una corrida anterior (ids >= BASE_ID) antes
    # de regenerar, para que archivos borrados de extra_docs/ no dejen restos.
    for stale in glob.glob(os.path.join(out_dir, "9[0-9][0-9][0-9][0-9][0-9][0-9]-*.md")):
        os.remove(stale)

    files = sorted(
        glob.glob(os.path.join(src_dir, "*.md"))
        + glob.glob(os.path.join(src_dir, "*.html"))
        + glob.glob(os.path.join(src_dir, "*.htm"))
    )

    new_rows = []
    next_id = BASE_ID
    for path in files:
        fname = os.path.basename(path)
        with open(path, encoding="utf-8", errors="replace") as f:
            raw = f.read()

        if path.lower().endswith((".html", ".htm")):
            body = html_to_text(raw)
        else:
            body = raw.strip()

        doc_title = extract_title(body, os.path.splitext(fname)[0].replace("-", " ").replace("_", " "))
        source_label = f"local:{src_dir.replace(os.sep, '/')}/{fname}"
        intro, sections = split_sections(body)

        # documento (title, content) a generar: si hay secciones H2, uno por
        # seccion (mas la intro si tiene contenido propio mas alla del H1);
        # si no, el documento entero como un unico articulo.
        pieces = []
        if sections:
            if intro and len(intro.splitlines()) > 3:
                pieces.append((doc_title, intro))
            for heading, section_body in sections:
                pieces.append((f"{doc_title} — {heading}", section_body))
        else:
            pieces.append((doc_title, body))

        for title, content in pieces:
            art_id = next_id
            next_id += 1
            slug = slugify(title)
            rel = f"articles/{art_id}-{slug}.md"
            out_path = os.path.join(out_dir, f"{art_id}-{slug}.md")

            frontmatter = (
                "---\n"
                f"title: \"{title}\"\n"
                f"source_id: {art_id}\n"
                f"source_url: \"{source_label}\"\n"
                f"{cfg['extra_note']}"
                "ingested_by: ingest_docs.py\n"
                "---\n\n"
            )
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(frontmatter + content + "\n")

            new_rows.append([str(art_id), title, rel, source_label])

    # reconstruir index.tsv: conservar filas no-"extra" (id < BASE_ID),
    # reemplazar el bloque extra con el resultado de esta corrida.
    existing = load_index(index_path)
    kept = [r for r in existing if not r[0].isdigit() or int(r[0]) < BASE_ID]
    all_rows = kept + new_rows
    os.makedirs(os.path.dirname(index_path) or ".", exist_ok=True)
    with open(index_path, "w", encoding="utf-8") as f:
        for r in all_rows:
            f.write("\t".join(r) + "\n")

    print(f"[{name}] {len(files)} documento(s) en {src_dir}/ -> {len(new_rows)} "
          f"articulo(s) extra en {out_dir}/ ; {index_path}: {len(kept)} fila(s) "
          f"preexistente(s) + {len(new_rows)} extra")


def main():
    which = sys.argv[1:] or list(TARGETS.keys())
    for name in which:
        if name not in TARGETS:
            print(f"target desconocido: {name} (opciones: {', '.join(TARGETS)})", file=sys.stderr)
            sys.exit(2)
        ingest_target(name, TARGETS[name])


if __name__ == "__main__":
    main()
