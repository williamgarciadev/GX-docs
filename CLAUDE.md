# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

`GX-docs` is a **GeneXus 18 documentation corpus** built to ground AI agents so
they answer with verifiable facts instead of hallucinating. The source is a full
dump of the official wiki (wiki.genexus.com); the repo turns that dump into a
clean, citable, retrieval-friendly corpus.

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
- `.claude/hooks/genexus_validate.py` — a `PostToolUse` (Write|Edit) hook that,
  after GeneXus code is written, extracts function/method calls and warns
  (non-blocking) about any name not in `corpus/api.tsv`. It self-skips files
  under `corpus/` and files without GeneXus code signals. User-defined
  procedures/SDT/BC methods are expected to surface (they aren't built-ins), so
  the message is advisory, not a hard block.
- Both hooks resolve the corpus location-independently so they work in-repo
  **and** installed globally, in this priority order: `$GENEXUS_CORPUS_DIR` →
  `$CLAUDE_CONFIG_DIR`(or `~/.claude`)`/genexus/corpus` → `$CLAUDE_PROJECT_DIR/corpus`.
- `install_global.sh` (macOS/Linux) / `install_global.ps1` (Windows) — copy the
  hooks + corpus to `~/.claude/genexus/` and merge both hooks into the **user**
  `settings.json` so they run in every project. Idempotent; the JSON merge logic
  is shared in `tools/genexus_install_merge.py`. See `INSTALL.md`.

## Common commands

- **Rebuild the corpus:** `python3 build_corpus.py` (reads `genexus_documentation.md`,
  overwrites `corpus/`). No dependencies beyond the Python 3 standard library.
- **Find an article:** grep `corpus/articles/` or `corpus/INDEX.md`; each filename
  is prefixed with its wiki id.
- **Validate the JSONL:** `python3 -c "import json;[json.loads(l) for l in open('corpus/genexus_corpus.jsonl')]"`

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

## Conventions

- **Preserve provenance.** Every article keeps its `source_url`. Anti-hallucination
  is the whole point: a GeneXus claim should be traceable to a `source_id`/`source_url`.
- **Don't hand-edit generated files.** Change `build_corpus.py` and regenerate
  so `genexus_documentation.md`, the `.md` articles, and the JSONL stay consistent.
- **Scope is GeneXus 18.** Don't generalize the corpus to other versions.
