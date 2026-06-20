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
  - `corpus/api.tsv` — verified API catalog (`name\tkind\turl`, 356 entries:
    127 functions, 203 methods, 26 commands) extracted from article titles.
    The hard anti-hallucination rule: a function/method/command not in this
    file does not exist in GeneXus 18.
  - `corpus/README.md` — schema and grounding usage rules.
- `INDICE_MAESTRO_GENEXUS.md` — a hand-curated learning index. Note: it
  references standalone topic files (`Variables.md`, `database-best-practices.md`,
  etc.) that are **not** in the repo — treat it as an aspirational map, not a file listing.
- `*.pdf` — GeneXus training PDFs (transactional integrity, DP language, etc.).
- `.claude/hooks/genexus_grounding.py` + `.claude/settings.json` — a
  `UserPromptSubmit` hook that, when a prompt looks GeneXus-related, retrieves
  matching articles from `corpus/index.tsv`, the relevant verified names from
  `corpus/api.tsv`, and injects a strict directive (hard rule: any
  function/method/command used must appear in `corpus/api.tsv`; verify against
  the corpus and cite `source_url`). This is the anti-hallucination guardrail.

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
images were never included in the dump). Re-running fully regenerates `corpus/`.

## Conventions

- **Preserve provenance.** Every article keeps its `source_url`. Anti-hallucination
  is the whole point: a GeneXus claim should be traceable to a `source_id`/`source_url`.
- **Don't hand-edit generated files.** Change `build_corpus.py` and regenerate
  so `genexus_documentation.md`, the `.md` articles, and the JSONL stay consistent.
- **Scope is GeneXus 18.** Don't generalize the corpus to other versions.
