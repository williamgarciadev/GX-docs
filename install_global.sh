#!/usr/bin/env bash
#
# Instala el grounding anti-alucinacion de GeneXus 18 (y Bantotal, si esta
# presente) de forma GLOBAL, para que los hooks corran en TODOS tus proyectos
# de Claude Code (no solo en este repo).
#
# Que hace:
#   1. Copia los hooks y el corpus GeneXus a  ~/.claude/genexus/
#      y, si existe, tambien corpus_bantotal/ (Bantotal es opcional)
#   2. Registra ambos hooks en tu settings de USUARIO  ~/.claude/settings.json
#      (UserPromptSubmit -> grounding ; PostToolUse Write|Edit -> validador),
#      fusionando sin pisar lo que ya tengas.
#
# Los hooks resuelven cada corpus en este orden:
#   $GENEXUS_CORPUS_DIR   -> ~/.claude/genexus/corpus          -> <proyecto>/corpus
#   $BANTOTAL_CORPUS_DIR  -> ~/.claude/genexus/corpus_bantotal -> <proyecto>/corpus_bantotal
# asi que tras instalar funcionan en cualquier carpeta.
#
# Uso:   ./install_global.sh         (instala/actualiza)
#        ./install_global.sh --dry-run   (muestra que haria, sin escribir)
#
# Requiere: bash, python3. Idempotente: re-ejecutar actualiza sin duplicar.
set -euo pipefail

DRY_RUN=0
[ "${1:-}" = "--dry-run" ] && DRY_RUN=1

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/genexus"
SETTINGS="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json"

echo "Origen : $SRC_DIR"
echo "Destino: $DEST"
echo "Settings: $SETTINGS"
echo

if [ ! -f "$SRC_DIR/corpus/api.tsv" ]; then
  echo "ERROR: no encuentro corpus/api.tsv en $SRC_DIR." >&2
  echo "Ejecuta primero  python3 build_corpus.py  para generar el corpus." >&2
  exit 1
fi

HAS_BANTOTAL=0
[ -f "$SRC_DIR/corpus_bantotal/tables.tsv" ] && HAS_BANTOTAL=1

if [ "$DRY_RUN" = "1" ]; then
  echo "[dry-run] Copiaria hooks -> $DEST/hooks/"
  echo "[dry-run] Copiaria corpus -> $DEST/corpus/"
  if [ "$HAS_BANTOTAL" = "1" ]; then
    echo "[dry-run] Copiaria corpus_bantotal -> $DEST/corpus_bantotal/"
  else
    echo "[dry-run] corpus_bantotal/ no encontrado, se omite (opcional)"
  fi
  echo "[dry-run] Fusionaria 2 hooks en $SETTINGS"
  exit 0
fi

# 1) copiar hooks + corpus
mkdir -p "$DEST/hooks" "$DEST/corpus"
cp "$SRC_DIR/.claude/hooks/genexus_grounding.py" "$DEST/hooks/"
cp "$SRC_DIR/.claude/hooks/genexus_validate.py" "$DEST/hooks/"
chmod +x "$DEST/hooks/"*.py
# corpus completo (catalogos .tsv, indices y articulos para poder leerlos)
cp -R "$SRC_DIR/corpus/." "$DEST/corpus/"
echo "Copiados hooks y corpus a $DEST"

# 1b) corpus Bantotal, si esta presente (opcional; no todo proyecto lo tiene)
if [ "$HAS_BANTOTAL" = "1" ]; then
  mkdir -p "$DEST/corpus_bantotal"
  cp -R "$SRC_DIR/corpus_bantotal/." "$DEST/corpus_bantotal/"
  echo "Copiado corpus_bantotal a $DEST/corpus_bantotal"
else
  echo "corpus_bantotal/ no encontrado en $SRC_DIR, se omite (opcional)"
fi

# 2) fusionar hooks en ~/.claude/settings.json (preservando lo existente)
G_CMD="python3 \"$DEST/hooks/genexus_grounding.py\" || true"
V_CMD="python3 \"$DEST/hooks/genexus_validate.py\" || true"
python3 "$SRC_DIR/tools/genexus_install_merge.py" "$SETTINGS" "$G_CMD" "$V_CMD"

echo
echo "Listo. Abre Claude Code y ejecuta /hooks una vez (o reinicia) para que"
echo "cargue los hooks globales. A partir de ahi corren en CUALQUIER proyecto."
