# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

`GX-docs` is a **GeneXus 18 documentation corpus** built to ground AI agents so
they answer with verifiable facts instead of hallucinating. The source is a full
dump of the official wiki (wiki.genexus.com); the repo turns that dump into a
clean, citable, retrieval-friendly corpus.

It also carries a second, smaller corpus for **Bantotal** (a banking core
built on top of GeneXus): `corpus_bantotal/`. Unlike GeneXus, Bantotal has no
public wiki, so that corpus is derived from a proprietary manual plus
(optionally) the user's own `.xpz` KB exports — see the "Bantotal" section
below for how it differs from the GeneXus corpus and its confidence levels.

## Layout

- `genexus_documentation.md` — the raw 16 MB / ~386k-line dump (5.433 articles,
  each as `# Title` + `File: NNNN.html`). **Source of truth; do not edit by hand.**
- `build_corpus.py` — transforms the dump into the corpus. Idempotent.
- `corpus/` — generated output (do not edit by hand; regenerate instead):
  - `corpus/articles/<id>-<slug>.md` — one cleaned article per file, with
    provenance frontmatter (`title`, `source_id`, `source_url`, `genexus_version`).
  - `corpus/genexus_corpus.jsonl` — one JSON record per article for embeddings/RAG.
  - `corpus/INDEX.md` — navigable index linking every article to its wiki source.
  - `corpus/index.tsv` — flat `id\ttitle\tpath\turl` index for fast lookup.
  - `corpus/api.tsv` — verified API catalog (`name\tkind\turl`, 546 entries:
    139 functions, 381 methods, 26 commands). Names come from: (a) article
    titles (`<Name> function|method|command`); (b) methods auto-scanned from
    bodies via the heading∩call rule (name appears both as a `#### [Name]`
    heading and a `.Name(` call in the same article); (c) functions auto-scanned
    from syntax blocks (`**Name(` bold-name-paren in an article that has
    "Type Returned"), with the kind decided corpus-wide (method if ever invoked
    as `.Name(`); (d) a small hand-seeded `EXTRA_API`. This captures API
    documented inside composite articles, e.g. the RegEx methods
    `IsMatch`/`Matches`/`ReplaceRegEx`/`SplitRegEx`. The hard anti-hallucination
    rule: a function/method/command not in this file does not exist in GeneXus 18.
  - `corpus/properties.tsv` — verified property catalog (`name\turl`, 1880
    entries; names are often multi-word, e.g. `Maximum length`). Names come
    from: (a) article titles (`<Name> property|properties`); (b) properties
    auto-scanned from composite-article bodies, where the author explicitly
    tags the name with the word "property" in a structured context — either as
    cross-reference link text (`[<Name> property](wiki-url)`) or as a whole
    table cell (`| <Name> property |`). The link/cell double-signal keeps it
    high-precision (free prose is excluded); the link's own target becomes the
    `source_url`. Same hard rule: a property not in this file does not exist in
    GeneXus 18.
  - `corpus/events.tsv` — verified event catalog (`name\turl`, 61 entries,
    e.g. `Start`, `IsValid`, `Refresh Grid`).
  - `corpus/datatypes.tsv` — verified Data Type catalog (`name\turl`, 127
    entries, e.g. `Boolean`, `Structured`, `VarChar`). Same hard rule applies
    to both.
  - `corpus/README.md` — schema and grounding usage rules.
- `bantotal_sources/` — raw Bantotal material (**source of truth for the
  Bantotal corpus; do not edit by hand**):
  - `MDU-99000-GL-V3R1.11.pdf` — the official Bantotal data-model manual
    (primary source; committed with the user's explicit authorization —
    it carries an "internal-use" license, be mindful before further
    redistributing it).
  - `Analisis_Modelo_Datos_Bantotal.md` — a derived technical analysis of the
    manual (118 pages, ~80 tables); source of `corpus_bantotal/tables.tsv`.
  - `Patron_9_Campos_Bantotal.md` — source of `corpus_bantotal/nine_fields.md`
    (the observed 9-base-field key pattern).
- `build_bantotal_corpus.py` — regenerates `corpus_bantotal/{tables,families}.tsv`
  and `nine_fields.md` from `bantotal_sources/`. Idempotent.
- `scan_bantotal_xpz.py` — regenerates `corpus_bantotal/xpz_objects.tsv` by
  parsing any `.xpz` files under `corpus_bantotal/bantotal_xpz/`. Idempotent;
  a no-op (empty output) until the user adds real KB exports there.
- `corpus_bantotal/` — generated Bantotal output (do not edit by hand):
  - `corpus_bantotal/tables.tsv` — `code\tname\tfamily\tnote\tsource` catalog
    of ~70 Bantotal tables (`FST017`, `FSD010`, ...). **Derived** from the
    secondary analysis, not a literal page-by-page PDF extraction — treat it
    as "this table exists, here's its purpose," not as an exhaustive or
    exact field list. For exact field structure, read
    `bantotal_sources/MDU-99000-GL-V3R1.11.pdf` directly.
  - `corpus_bantotal/families.tsv` — table-prefix taxonomy (`FST`, `FSD`,
    `FSR`, `FSH`, `FSN`, ...): `prefix\tcategory\tpurpose`.
  - `corpus_bantotal/nine_fields.md` — the 9-base-field key pattern
    (`PGCOD` + 8 fields with a 2-letter context prefix). Presented as an
    observed heuristic, not a guaranteed rule — confirm against the specific
    table before assuming it applies.
  - `corpus_bantotal/xpz_objects.tsv` — `name\ttype\tmodule\tattributes_or_vars\tsource_xpz`
    catalog of objects (Transaction/Procedure/SDT/...) scanned from the
    user's own `.xpz` KB exports. **Highest-confidence** Bantotal source —
    it comes from real KB XML, not prose — but empty until the user drops
    `.xpz` files into `corpus_bantotal/bantotal_xpz/` and runs
    `scan_bantotal_xpz.py`.
  - `corpus_bantotal/bantotal_xpz/` — drop `.xpz` KB exports here.
  - `corpus_bantotal/index.tsv` + `corpus_bantotal/articles/` — articles
    ingested via `ingest_docs.py bantotal` from `extra_docs/bantotal/`
    (same `id\ttitle\tpath\turl` shape as `corpus/index.tsv`, empty until you
    ingest something).
  - `corpus_bantotal/README.md` — schema, confidence levels, and grounding
    usage rules for the Bantotal corpus.
- `extra_docs/genexus/`, `extra_docs/bantotal/` — drop-in folders for your own
  `.md`/`.html` documents (notes, extra manuals, anything not already covered).
  `python3 ingest_docs.py [genexus|bantotal]` converts each file into a
  citable article (`corpus/articles/9000001-....md` or
  `corpus_bantotal/articles/9000001-....md`, synthetic ids starting at
  `9000001` so they never collide with real wiki ids) and rebuilds the
  matching `index.tsv`. Their `source_url` is `local:extra_docs/<target>/<file>`
  — **not** a wiki.genexus.com URL — so the grounding hook and the agent never
  cite them as if they were official documentation. Idempotent: delete a file
  from `extra_docs/` and its generated article disappears on the next run.
  If a document has 2+ `## ` headings (a "cheatsheet" covering many topics
  under one title), it's split into one article per section (title =
  `"<doc title> — <heading>"`) plus an intro article for anything before the
  first heading — otherwise a long multi-topic doc would be nearly
  unfindable, since the grounding hook ranks articles by title match, not
  full-body search.
- `ingest_docs.py` — the ingestion script above. HTML is converted to plain
  markdown-ish text with a small stdlib-only `html.parser` based converter (no
  external deps); `.md` files are used as-is.
- `INDICE_MAESTRO_GENEXUS.md` — a hand-curated learning index. Note: it
  references standalone topic files (`Variables.md`, `database-best-practices.md`,
  etc.) that are **not** in the repo — treat it as an aspirational map, not a file listing.
- `*.pdf` — GeneXus training PDFs (transactional integrity, DP language, etc.).
- `.claude/hooks/genexus_grounding.py` + `.claude/settings.json` — a
  `UserPromptSubmit` hook that, when a prompt looks GeneXus-related, retrieves
  matching articles from `corpus/index.tsv`, the relevant verified names from
  the verified catalogs (`api.tsv`, `properties.tsv`, `events.tsv`,
  `datatypes.tsv`), and injects a strict directive (hard rule: any
  function/method/command/property/event/Data Type used must appear in those
  catalogs; verify against the corpus and cite `source_url`). This is the
  anti-hallucination guardrail. If a GeneXus-related prompt yields **no** local
  match, the hook injects a fallback telling the agent to verify against the
  live official wiki (`WebSearch site:wiki.genexus.com <terms>` / `WebFetch`)
  and cite the real URL — never invent when offline.
  The same hook also detects Bantotal-related prompts independently of the
  GeneXus triggers: a fixed keyword list (`BANTOTAL_TRIGGERS`: "bantotal",
  "9 campos", ...), a bare table code like `FST017`, or — since a fixed list
  always lags what gets ingested — a **dynamic** check (`bantotal_dynamic_vocab`)
  that matches the prompt against words actually present in
  `corpus_bantotal/index.tsv` titles and `tables.tsv` names/notes. This is
  what lets a prompt about "ACH" or "garantías" trigger grounding once an
  ingested article covers that topic, without hand-maintaining the keyword
  list. It then injects a directive sourced from `corpus_bantotal/tables.tsv`,
  `xpz_objects.tsv`, and `index.tsv` (articles ingested via `ingest_docs.py`)
  — with no web fallback, since there's no public wiki; the fallback there is
  to say so explicitly and point at `bantotal_sources/MDU-99000-GL-V3R1.11.pdf`
  or ask the user for the relevant `.xpz`. Article ranking (`rank_articles`)
  is shared between the GeneXus and Bantotal sections.
- `.claude/hooks/genexus_validate.py` — a `PostToolUse` (Write|Edit) hook that,
  after GeneXus code is written, extracts function/method calls and warns
  (non-blocking) about any name not in `corpus/api.tsv`. It self-skips files
  under `corpus/` and files without GeneXus code signals. User-defined
  procedures/SDT/BC methods are expected to surface (they aren't built-ins), so
  the message is advisory, not a hard block.
  The same hook also scans for Bantotal-style table codes
  (`FS[A-Z]\d{3}`, e.g. `FST017`, `FSD010`) and warns (also non-blocking) about
  any code not present in `corpus_bantotal/tables.tsv` — since that catalog is
  derived and not exhaustive, a flagged code may be a real table missing from
  it rather than an invented one.
- Both hooks resolve the corpora location-independently so they work in-repo
  **and** installed globally, in this priority order: `$GENEXUS_CORPUS_DIR` →
  `$CLAUDE_CONFIG_DIR`(or `~/.claude`)`/genexus/corpus` → `$CLAUDE_PROJECT_DIR/corpus`
  for GeneXus, and `$BANTOTAL_CORPUS_DIR` →
  `$CLAUDE_CONFIG_DIR`(or `~/.claude`)`/genexus/corpus_bantotal` →
  `$CLAUDE_PROJECT_DIR/corpus_bantotal` for Bantotal.
- `install_global.sh` (macOS/Linux) / `install_global.ps1` (Windows, or
  double-click `install_global.bat`) — copy the hooks + corpus to
  `~/.claude/genexus/` and merge both hooks into the **user** `settings.json` so
  they run in every project. Idempotent; the JSON merge logic is shared in
  `tools/genexus_install_merge.py`. See `INSTALL.md`.

## Common commands

- **Rebuild the corpus:** `python3 build_corpus.py` (reads `genexus_documentation.md`,
  overwrites `corpus/`). No dependencies beyond the Python 3 standard library.
- **Find an article:** grep `corpus/articles/` or `corpus/INDEX.md`; each filename
  is prefixed with its wiki id.
- **Validate the JSONL:** `python3 -c "import json;[json.loads(l) for l in open('corpus/genexus_corpus.jsonl')]"`
- **Rebuild the Bantotal corpus:** `python3 build_bantotal_corpus.py` (reads
  `bantotal_sources/`, overwrites `corpus_bantotal/{tables,families}.tsv` and
  `nine_fields.md`; leaves `xpz_objects.tsv` alone).
- **Catalog real KB objects:** drop `.xpz` exports into
  `corpus_bantotal/bantotal_xpz/`, then `python3 scan_bantotal_xpz.py`
  (regenerates `corpus_bantotal/xpz_objects.tsv`).
- **Ingest your own `.md`/`.html` docs:** drop files into
  `extra_docs/genexus/` and/or `extra_docs/bantotal/`, then
  `python3 ingest_docs.py` (or `... genexus` / `... bantotal` for just one).

## How the build works

`build_corpus.py` splits the dump on each `File: NNNN.html` marker (the preceding
`# ` line is the title), then per article: removes the duplicated H1 title and the
`File:`/`Newest Version` wiki cruft, rewrites internal `NNNN.html` links to absolute
`https://wiki.genexus.com/commwiki/wiki?NNNN` URLs, and replaces broken
`./images/NNNN.*` embeds with a `` `[imagen omitida: wiki id N]` `` marker (the
images were never included in the dump). It also derives the lookup/catalog
files (`index.tsv`, `api.tsv`, `properties.tsv`, `events.tsv`, `datatypes.tsv`)
— including scanning article bodies for documented methods, functions, and
properties (the latter via the tagged link/cell signal). Re-running fully
regenerates `corpus/`.

`build_bantotal_corpus.py` parses `bantotal_sources/Analisis_Modelo_Datos_Bantotal.md`
for table rows (`| **CODE** | name | note |`), keeps the first occurrence per
code, and tags each with a `family` from the fixed prefix taxonomy (FST, FSD,
FSR, FSE, FSH, FSX, FSA, FSI, FSM, FSN). It does **not** parse the PDF itself —
the PDF is carried as the citable primary source, not as build input.
`scan_bantotal_xpz.py` parses `.xpz` (zipped GeneXus KB export XML) directly:
object GUIDs → type names, `Transaction_Structure`/`SDT_Structure` parts →
attribute/item names, `Variables` parts → variable names.

## Conventions

- **Preserve provenance.** Every article keeps its `source_url`. Anti-hallucination
  is the whole point: a GeneXus claim should be traceable to a `source_id`/`source_url`.
- **Don't hand-edit generated files.** Change `build_corpus.py` and regenerate
  so `genexus_documentation.md`, the `.md` articles, and the JSONL stay consistent.
  Same for `corpus_bantotal/`: change `build_bantotal_corpus.py` /
  `scan_bantotal_xpz.py`, not the generated `.tsv`/`.md` files.
- **Scope is GeneXus 18.** Don't generalize the `corpus/` corpus to other
  versions.
- **Bantotal catalog is derived, not exhaustive.** `corpus_bantotal/tables.tsv`
  says a table exists and roughly what it's for; it is not proof a table is
  *absent* if missing, and it does not give exact field structure — that
  requires reading `bantotal_sources/MDU-99000-GL-V3R1.11.pdf` directly.
  `corpus_bantotal/xpz_objects.tsv` (from real `.xpz`) is higher-confidence
  than `tables.tsv` (from a secondary written analysis) whenever both apply.
