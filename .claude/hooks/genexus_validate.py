#!/usr/bin/env python3
"""
Hook PostToolUse (Write|Edit): valida codigo GeneXus recien escrito contra los
catalogos verificados (`corpus/api.tsv` + `properties.tsv`/`events.tsv`/
`datatypes.tsv`). Si encuentra llamadas a funciones/metodos que NO existen en
ninguno de esos catalogos, avisa (no bloquea) para que el agente las revise y no
deje codigo con API alucinada.

El set "bueno" incluye las 4 fuentes a proposito: muchos accesores que el regex
captura como `.Metodo` son en realidad PROPIEDADES (`.Visible`, `.Enabled`) o
nombres de Data Type; si solo se comparara contra api.tsv se marcarian como
alucinados siendo validos. Foliar los 4 catalogos elimina ese falso positivo y
deja marcado solo lo verdaderamente desconocido.

Es advisory por diseno: las llamadas a procedimientos, SDT y Business Components
del usuario tambien apareceran como "no reconocidas" (no estan en el catalogo de
built-ins), por eso el mensaje lo aclara y NO bloquea la escritura.
"""
import json
import os
import re
import sys

# Extensiones que NUNCA son codigo GeneXus suelto: tooling, docs y fuentes de
# otros lenguajes. Se descartan ANTES de buscar senales, porque un .py/.md puede
# contener los literales "for each"/"Do Case" (p. ej. el propio codigo de estos
# hooks) y disparar un falso positivo. El codigo GeneXus volcado a disco suele ir
# en .txt/.gx/.xml o sin extension, que NO se filtran aqui.
SKIP_EXTS = {
    ".py", ".md", ".markdown", ".json", ".js", ".jsx", ".ts", ".tsx",
    ".sh", ".bash", ".ps1", ".bat", ".cmd", ".yml", ".yaml", ".toml",
    ".ini", ".cfg", ".css", ".scss", ".cs", ".java", ".go", ".rb", ".php",
}

# Senales de que el archivo contiene codigo GeneXus (evita disparar en
# Python/Markdown/prosa). Basta una.
GX_SIGNALS = [
    r"\bEndSub\b", r"\bSub\s+'", r"\bDo\s+'", r"\bFor\s+each\b", r"\bEndfor\b",
    r"\bDo\s+Case\b", r"\bEndCase\b", r"\bEndIf\b", r"\bEndFor\b", r"\bEndDo\b",
]
gx_signal_re = re.compile("|".join(GX_SIGNALS), re.IGNORECASE)

# Llamadas estilo funcion  Nombre(   y estilo metodo  .Nombre(
func_call_re = re.compile(r"(?<![.\w])([A-Za-z][A-Za-z0-9_]*)\s*\(")
meth_call_re = re.compile(r"\.([A-Za-z][A-Za-z0-9_]*)\s*\(")

# Comentarios GeneXus: bloque /* ... */ y linea // ... . Se eliminan ANTES de
# buscar llamadas para no marcar prosa de comentarios (p. ej. "esperadas (...")
# como funciones. El "//" de linea exige no ir precedido de ":" para no romper
# URLs dentro de literales de cadena ("https://...").
block_comment_re = re.compile(r"/\*.*?\*/", re.DOTALL)
line_comment_re = re.compile(r"(?<!:)//[^\n]*")


def strip_comments(text):
    text = block_comment_re.sub(" ", text)
    text = line_comment_re.sub(" ", text)
    return text

# Palabras clave / comandos del lenguaje que pueden ir seguidos de "(" y NO son
# funciones del catalogo. No deben marcarse como sospechosas.
KEYWORDS = {
    "if", "then", "else", "elsif", "endif", "while", "endwhile", "for", "each",
    "endfor", "do", "case", "endcase", "when", "otherwise", "sub", "endsub",
    "new", "endnew", "return", "exit", "call", "where", "and", "or", "not",
    "in", "like", "by", "order", "defined", "true", "false", "null", "noaccept",
}


def project_dir():
    return os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def corpus_dir():
    """Resuelve el corpus para funcionar dentro del repo o instalado global.
    Prioridad: $GENEXUS_CORPUS_DIR -> ~/.claude/genexus/corpus -> proyecto."""
    env = os.environ.get("GENEXUS_CORPUS_DIR")
    if env and os.path.isdir(env):
        return env
    cfg = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude")
    glob = os.path.join(cfg, "genexus", "corpus")
    if os.path.isdir(glob):
        return glob
    return os.path.join(project_dir(), "corpus")


def load_names(path):
    """Devuelve (todos, funciones_y_comandos, metodos) en minusculas."""
    alln, funcs, meths = set(), set(), set()
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                p = line.rstrip("\n").split("\t")
                if len(p) != 3:
                    continue
                name, kind = p[0].lower(), p[1]
                alln.add(name)
                if kind == "method":
                    meths.add(name)
                else:
                    funcs.add(name)
    except OSError:
        pass
    return alln, funcs, meths


def load_catalog_names(path):
    """Nombres (primera columna) de un catalogo TSV simple, en minusculas.
    Sirve para properties.tsv / events.tsv / datatypes.tsv (formato name\\turl).
    Los nombres multipalabra ('Maximum length') quedan inertes para el chequeo
    de llamadas (que compara tokens sueltos); solo los de una palabra (Visible,
    Boolean, Back) aportan, que es justo lo que evita el falso positivo."""
    names = set()
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                p = line.rstrip("\n").split("\t")
                if p and p[0]:
                    names.add(p[0].lower())
    except OSError:
        pass
    return names


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path") or ""
    if not path or not os.path.isfile(path):
        return

    # Gate por extension: descarta tooling/docs/otros lenguajes antes de leer.
    if os.path.splitext(path)[1].lower() in SKIP_EXTS:
        return

    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            content = f.read()
    except OSError:
        return

    # No validar los propios ficheros del corpus/repo (estan llenos de
    # nombres de API legitimos en prosa) ni archivos sin senales GeneXus.
    norm_path = path.replace("\\", "/")
    if "/corpus/" in norm_path or norm_path.endswith(".tsv"):
        return
    if not gx_signal_re.search(content):
        return

    # descartar comentarios: su prosa no es codigo y genera falsos positivos
    content = strip_comments(content)

    base = project_dir()
    cdir = corpus_dir()
    alln, funcs, meths = load_names(os.path.join(cdir, "api.tsv"))
    if not alln:
        return

    # Set "bueno": api.tsv + properties + events + datatypes. Foliar los 3
    # catalogos extra evita marcar como alucinados accesores validos de una
    # palabra (`.Visible`, `.Enabled`) o nombres de Data Type (`Boolean`).
    known = set(alln)
    for cat in ("properties.tsv", "events.tsv", "datatypes.tsv"):
        known |= load_catalog_names(os.path.join(cdir, cat))

    # candidatos: ultima aparicion gana; preservar nombre original para mostrar
    func_cands, meth_cands = {}, {}
    for m in func_call_re.finditer(content):
        n = m.group(1)
        if n.lower() not in KEYWORDS:
            func_cands[n.lower()] = n
    for m in meth_call_re.finditer(content):
        n = m.group(1)
        meth_cands[n.lower()] = n

    # Para validar EXISTENCIA del nombre, ambas formas se comparan contra todo
    # el catalogo: la distincion funcion/metodo es de estilo, no de existencia
    # (muchas "funciones" se invocan como metodo sobre tipos de dato).
    bad_funcs = sorted({orig for low, orig in func_cands.items() if low not in known})
    bad_meths = sorted({orig for low, orig in meth_cands.items() if low not in known})

    if not bad_funcs and not bad_meths:
        return  # todo verificado -> silencioso

    lines = [
        "## Validacion GeneXus (anti-alucinacion)",
        "",
        f"En `{os.path.relpath(path, base)}` hay llamadas que NO figuran en",
        "NINGUN catalogo verificado (api/properties/events/datatypes). Revisa cada",
        "una: si es API/propiedad/Data Type built-in de GeneXus 18, debe existir en",
        "su catalogo (si no esta, NO existe y hay que corregirla); si es un",
        "Procedimiento/SDT/Business Component TUYO, esta bien (no se cataloga aqui).",
        "Verifica con: "
        f"grep -i \"^<nombre>\" {os.path.join(cdir, '*.tsv')}",
    ]
    if bad_funcs:
        lines += ["", "Funciones no reconocidas: " + ", ".join(bad_funcs[:15])]
    if bad_meths:
        lines += [
            "",
            "Metodos no reconocidos (a menudo metodos de SDT/BC del usuario, "
            "confirma): " + ", ".join(bad_meths[:15]),
        ]

    out = {
        "systemMessage": "Validacion GeneXus: revisa nombres no catalogados ("
        + ", ".join((bad_funcs + bad_meths)[:8]) + ")",
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "\n".join(lines),
        },
    }
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
