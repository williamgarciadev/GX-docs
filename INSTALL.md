# Instalación global del grounding GeneXus

Por defecto los hooks anti-alucinación solo actúan dentro de este repo (vía
`.claude/settings.json`). Para que corran en **todos** tus proyectos de Claude
Code, instálalos en tu configuración de **usuario**.

Qué hace el instalador:

1. Copia los hooks y el corpus a `~/.claude/genexus/` (en Windows
   `%USERPROFILE%\.claude\genexus\`).
2. Registra ambos hooks en tu `~/.claude/settings.json` (settings de usuario =
   todos los proyectos), **fusionando** sin pisar lo que ya tengas.

Los hooks resuelven el corpus en este orden, así que tras instalar funcionan
desde cualquier carpeta:

```
$GENEXUS_CORPUS_DIR  ->  ~/.claude/genexus/corpus  ->  <proyecto>/corpus
```

> Requisito: Python 3 en el PATH. Los instaladores son **idempotentes**:
> re-ejecutarlos actualiza el corpus/hooks sin duplicar la configuración.

---

## Windows 11 (Claude Code CLI)

**La forma más fácil:** haz **doble clic** en `install_global.bat`. Lanza el
instalador en una ventana que se queda abierta para que veas el resultado (no
necesita permisos de administrador).

O desde **PowerShell** en la carpeta del repo:

```powershell
./install_global.ps1
```

Si PowerShell bloquea el script por la política de ejecución:

```powershell
powershell -ExecutionPolicy Bypass -File .\install_global.ps1
```

Ver qué haría sin escribir nada: `./install_global.ps1 -DryRun`

> El script detecta tu intérprete (`python`, `python3` o `py`) y registra el
> comando del hook como `python "C:\Users\<tu-usuario>\.claude\genexus\hooks\..."`.

**Alternativa con Git Bash / WSL:** si prefieres bash, puedes usar el script
`.sh` (sección siguiente) desde Git Bash o una distro WSL.

## macOS / Linux

```bash
./install_global.sh           # instala/actualiza
./install_global.sh --dry-run # muestra qué haría
```

---

## Paso final (obligatorio)

Tras instalar, abre Claude Code y ejecuta **`/hooks`** una vez (o reinicia la
CLI) para que cargue los hooks recién añadidos a tu settings de usuario. A
partir de ahí corren en cualquier proyecto.

Comprueba que están activos en `/hooks`: deberías ver `genexus_grounding.py`
(UserPromptSubmit) y `genexus_validate.py` (PostToolUse, matcher `Write|Edit`).

---

## Actualizar el corpus

Si regeneras el corpus (`python3 build_corpus.py`), vuelve a ejecutar el
instalador para copiar los catálogos nuevos a la ubicación global:

```bash
python3 build_corpus.py && ./install_global.sh     # (o ./install_global.ps1 en Windows)
```

## Desinstalar

1. Borra la carpeta `~/.claude/genexus/` (Windows: `%USERPROFILE%\.claude\genexus\`).
2. Edita `~/.claude/settings.json` y quita las dos entradas de hooks cuyo
   `command` apunta a `genexus_grounding.py` / `genexus_validate.py`.

## Mantenerlo solo en este proyecto

No hagas nada: el `.claude/settings.json` del repo ya activa los hooks aquí.
Si instalaste en global y solo quieres dejarlo por proyecto, desinstala (arriba).
