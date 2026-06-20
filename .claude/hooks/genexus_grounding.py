#!/usr/bin/env python3
"""
Hook UserPromptSubmit: ancla (grounding) las respuestas sobre GeneXus en el
corpus local (corpus/) para que el agente NO invente funciones, metodos o
comandos que GeneXus no tiene.

Cuando el prompt parece pedir codigo/ayuda GeneXus, este hook:
  1. busca en corpus/index.tsv los articulos cuyos titulos mejor coinciden
  2. inyecta (additionalContext) una directiva estricta + la lista de
     articulos relevantes (titulo, ruta local y source_url) que el agente
     debe leer y citar antes de responder.

No requiere dependencias externas (solo stdlib). Es de solo lectura.
"""
import json
import os
import re
import sys
import unicodedata

MAX_ARTICLES = 8

# Senales de que el prompt es sobre desarrollo GeneXus.
TRIGGERS = {
    "genexus", "gx", "subrutina", "subrutinas", "subroutine", "for each",
    "foreach", "business component", "transaccion", "transaction", "webpanel",
    "web panel", "procedimiento", "procedure", "proc", "data provider",
    "dataprovider", "sdt", "domain", "dominio", "rule", "regla", "grid",
    "atributo", "attribute", "do case", "do while", "parm", "udp", "&",
    "panel object", "knowledge base", "gam", "data type",
}

# Palabras a ignorar al puntuar coincidencias de titulo (ruido o demasiado
# comunes en el corpus, como "genexus", que apareceria en cientos de titulos).
STOP = {
    "the", "and", "for", "with", "que", "una", "uno", "los", "las", "del",
    "para", "por", "con", "como", "crea", "crear", "creame", "hazme", "haz",
    "necesito", "quiero", "dame", "un", "una", "de", "la", "el", "en", "a",
    "me", "mi", "se", "su", "lo", "al", "es", "o", "y",
    "create", "make", "need", "want", "please", "porfavor", "object",
    "genexus", "gx", "how", "howto", "use", "using", "que",
    "uso", "usar", "usando", "utilizar", "utiliza", "como", "cómo",
}

# Sinonimos ES->EN (los titulos del corpus estan casi todos en ingles).
# Cada token de la consulta se expande con su equivalente para mejorar recall.
SYNONYMS = {
    "subrutina": "subroutine", "subrutinas": "subroutine",
    "validar": "validate", "validacion": "validation", "valida": "validate",
    "correo": "email", "correos": "email", "mail": "email",
    "procedimiento": "procedure", "procedimientos": "procedure",
    "dominio": "domain", "dominios": "domain",
    "regla": "rule", "reglas": "rule",
    "cadena": "string", "texto": "string",
    "fecha": "date", "numero": "numeric", "entero": "integer",
    "transaccion": "transaction", "transacciones": "transaction",
    "atributo": "attribute", "atributos": "attribute",
    "variable": "variable", "variables": "variable",
    "evento": "event", "eventos": "event",
    "formato": "format", "funcion": "function", "funciones": "function",
    "metodo": "method", "metodos": "method", "propiedad": "property",
    "consulta": "query", "tabla": "table", "tablas": "table",
}


def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )


def norm(s):
    return strip_accents(s.lower())


def tokens(s):
    return [t for t in re.split(r"[^a-z0-9&]+", norm(s)) if t]


def project_dir():
    return os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def corpus_dir():
    """Resuelve el directorio del corpus para que el hook funcione tanto dentro
    de este repo como instalado globalmente. Orden de prioridad:
      1. $GENEXUS_CORPUS_DIR  (override explicito)
      2. ~/.claude/genexus/corpus  (instalacion global del usuario)
      3. $CLAUDE_PROJECT_DIR/corpus  (este proyecto)
    """
    env = os.environ.get("GENEXUS_CORPUS_DIR")
    if env and os.path.isdir(env):
        return env
    cfg = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude")
    glob = os.path.join(cfg, "genexus", "corpus")
    if os.path.isdir(glob):
        return glob
    return os.path.join(project_dir(), "corpus")


def load_index(path):
    rows = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) == 4:
                    rows.append(parts)  # id, title, rel, url
    except OSError:
        pass
    return rows


def load_api(path):
    """Catalogo de API verificada: lista de (name, kind, url)."""
    api = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) == 3:
                    api.append(parts)  # name, kind, url
    except OSError:
        pass
    return api


def load_props(path):
    """Catalogo de propiedades verificadas: lista de (name, url)."""
    props = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) == 2:
                    props.append(parts)  # name, url
    except OSError:
        pass
    return props


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return  # sin salida -> no se inyecta nada
    prompt = data.get("prompt", "") or ""
    np = norm(prompt)

    # Solo actuar si el prompt huele a GeneXus.
    if not any(t in np for t in TRIGGERS):
        return

    cdir = corpus_dir()
    corpus = lambda *p: os.path.join(cdir, *p)
    rows = load_index(corpus("index.tsv"))
    api = load_api(corpus("api.tsv"))
    props = load_props(corpus("properties.tsv"))
    events = load_props(corpus("events.tsv"))
    datatypes = load_props(corpus("datatypes.tsv"))
    if not rows and not api:
        return

    # Etiqueta amigable para los textos: "corpus" si el corpus esta dentro del
    # proyecto actual; la ruta absoluta si es una instalacion global (asi las
    # referencias a archivos resuelven desde cualquier proyecto).
    proj = os.path.abspath(project_dir())
    clabel = "corpus" if os.path.abspath(cdir).startswith(proj + os.sep) else cdir

    # tokens de la consulta (+ sinonimos ES->EN), sin stopwords.
    # base_tokens conserva los terminos originales (para la busqueda web).
    qtokens = set()
    base_tokens = []
    for t in tokens(prompt):
        if t in STOP or len(t) < 3:
            continue
        if t not in base_tokens:
            base_tokens.append(t)
        qtokens.add(t)
        if t in SYNONYMS:
            qtokens.add(SYNONYMS[t])

    def matches(q, ttoks):
        # coincidencia exacta, o raiz comun de 5 chars (stemming ligero:
        # "validate"~"validation"~"validationtype"). Evita falsos positivos
        # por subcadena como "date" dentro de "validate".
        for tt in ttoks:
            if q == tt:
                return True
            if len(q) >= 5 and len(tt) >= 5 and q[:5] == tt[:5]:
                return True
        return False

    scored = []
    if qtokens:
        for art_id, title, rel, url in rows:
            ttoks = set(tokens(title))
            hits = [q for q in qtokens if matches(q, ttoks)]
            if hits:
                # peso: nº de coincidencias + bonus por tokens largos;
                # se penaliza un titulo muy largo (menos especifico)
                score = sum(1 + (len(w) >= 5) for w in hits) - 0.02 * len(ttoks)
                scored.append((score, art_id, title, rel, url))
        scored.sort(key=lambda r: (-r[0], int(r[1])))

    top = scored[:MAX_ARTICLES]

    # nombres de API verificada relevantes a la consulta (match por stem)
    n_func = sum(1 for _n, k, _u in api if k == "function")
    n_meth = sum(1 for _n, k, _u in api if k == "method")
    n_cmd = sum(1 for _n, k, _u in api if k == "command")
    rel_api = []
    if qtokens:
        for name, kind, url in api:
            if matches(norm(name), qtokens) or norm(name) in qtokens:
                rel_api.append((name, kind, url))
    rel_api = rel_api[:12]

    # Ranking para catalogos de nombres multipalabra (propiedades, eventos,
    # Data Types). Se puntua con frecuencia inversa para que un token-comodin
    # (p. ej. "attribute", que matchea cientos de propiedades) pese mucho menos
    # que uno especifico (p. ej. "length"), y el nombre pertinente quede arriba.
    def rank_multiword(catalog, limit=10):
        if not qtokens or not catalog:
            return []
        toks = [(name, url, set(tokens(name))) for name, url in catalog]
        df = {q: sum(1 for _n, _u, nt in toks if matches(q, nt)) for q in qtokens}
        scored = []
        for name, url, ntoks in toks:
            hit = [q for q in qtokens if df[q] and matches(q, ntoks)]
            if hit:
                score = sum(1.0 / df[q] for q in hit)
                scored.append((score, len(name), name, url))
        scored.sort(key=lambda r: (-r[0], r[1]))
        return [(n, u) for _s, _l, n, u in scored[:limit]]

    rel_props = rank_multiword(props, 10)
    rel_events = rank_multiword(events, 8)
    rel_dts = rank_multiword(datatypes, 8)

    lines = [
        "## GROUNDING GeneXus (anti-alucinacion)",
        "",
        f"Tienes disponible el corpus OFICIAL de GeneXus 18 en `{clabel}/`.",
        "Antes de escribir o describir codigo GeneXus (subrutinas, procedimientos,",
        "For Each, Business Components, Data Types, funciones, metodos, comandos):",
        "",
        "1. NO inventes funciones, metodos, propiedades, comandos, eventos ni",
        "   Data Types. Usa solo los que aparezcan en el corpus.",
        "2. REGLA DURA: todo nombre que uses DEBE figurar en el catalogo verificado",
        "   correspondiente; si NO esta ahi, NO existe en GeneXus 18, no lo uses:",
        f"     - funciones/metodos/comandos -> `{clabel}/api.tsv` ({n_func} func, "
        f"{n_meth} met, {n_cmd} cmd)",
        f"     - propiedades                -> `{clabel}/properties.tsv` ({len(props)})",
        f"     - eventos                    -> `{clabel}/events.tsv` ({len(events)})",
        f"     - Data Types                 -> `{clabel}/datatypes.tsv` ({len(datatypes)})",
        f"   Comprueba con: grep -i \"^<nombre>\\b\" {clabel}/api.tsv {clabel}/*.tsv",
        "3. Verifica la sintaxis exacta leyendo el articulo del nombre en",
        f"   `{clabel}/articles/` (o el `source_url` del catalogo).",
        "4. Cita el `source_url` del articulo en el que te apoyas.",
        "5. Si NO encuentras respaldo en el corpus, dilo explicitamente en vez de",
        "   suponer; no rellenes huecos con APIs de otros lenguajes (no inventes",
        "   cosas tipo `email.IsValid()` si no estan en el catalogo).",
    ]

    if rel_api:
        lines += [
            "",
            "Nombres de API verificada que podrian aplicar a esta consulta",
            "(nombre | tipo | fuente):",
            "",
        ]
        for name, kind, url in rel_api:
            lines.append(f"- {name} | {kind} | {url}")

    if rel_props:
        lines += [
            "",
            "Propiedades verificadas que podrian aplicar (nombre | fuente):",
            "",
        ]
        for name, url in rel_props:
            lines.append(f"- {name} | property | {url}")

    if rel_events:
        lines += [
            "",
            "Eventos verificados que podrian aplicar (nombre | fuente):",
            "",
        ]
        for name, url in rel_events:
            lines.append(f"- {name} | event | {url}")

    if rel_dts:
        lines += [
            "",
            "Data Types verificados que podrian aplicar (nombre | fuente):",
            "",
        ]
        for name, url in rel_dts:
            lines.append(f"- {name} | data type | {url}")

    if top:
        lines += [
            "",
            "Articulos del corpus posiblemente relevantes para esta consulta",
            "(leelos antes de responder):",
            "",
        ]
        for _score, art_id, title, rel, url in top:
            lines.append(f"- {title} -> `{clabel}/{rel}`  ({url})")

    # FALLBACK: si NO hubo ninguna coincidencia local (ni articulos, ni nombres
    # en los catalogos), no te quedes sin fuente: ve a la wiki OFICIAL en linea.
    any_local = bool(top or rel_api or rel_props or rel_events or rel_dts)
    if not any_local:
        terms = " ".join(base_tokens) or prompt.strip()
        lines += [
            "",
            "### FALLBACK: sin coincidencia en el corpus local",
            "",
            "No hubo coincidencia ni en `corpus/articles/` ni en los catalogos",
            "(api/properties/events/datatypes). Antes de responder, VERIFICA en la",
            "documentacion OFICIAL en linea (no inventes):",
            "",
            f"1. WebSearch:  site:wiki.genexus.com {terms}",
            "2. Abre con WebFetch la pagina de `wiki.genexus.com` mas pertinente",
            "   y extrae de ahi funciones/sintaxis/propiedades reales.",
            "3. Cita la URL real de wiki.genexus.com de la que tomes la informacion.",
            "4. Si NO hay acceso a la red, DILO explicitamente y no respondas con",
            "   nombres/sintaxis que no puedas verificar; no rellenes con otros",
            "   lenguajes ni inventes APIs.",
            "",
            "La REGLA DURA sigue vigente: solo usa nombres verificables en el",
            "corpus local O en wiki.genexus.com.",
        ]

    out = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "\n".join(lines),
        }
    }
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
