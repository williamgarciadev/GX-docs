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

## Paso 1 — Requisitos y clonar el repo

Necesitas **Git** y **Python 3** instalados (el corpus ya viene versionado, no
hay que construir nada).

### Windows 11

1. Instala **Git for Windows**: https://git-scm.com/download/win (incluye Git Bash).
2. Instala **Python 3**: https://www.python.org/downloads/windows/ — en el
   instalador marca **"Add python.exe to PATH"**.
3. Cierra y reabre la terminal para que el PATH se actualice. Comprueba:
   ```powershell
   git --version
   python --version
   ```
4. Clona el repo (en la carpeta donde guardes tus proyectos, p. ej. tu usuario):
   ```powershell
   cd %USERPROFILE%
   git clone https://github.com/williamgarciadev/GX-docs.git
   cd GX-docs
   ```
   > No necesitas indicar la rama: el repositorio usa la rama de trabajo como
   > **predeterminada**, así que `git clone` ya descarga todo y te sitúa en ella.

### macOS / Linux

```bash
git clone https://github.com/williamgarciadev/GX-docs.git
cd GX-docs
```

Ya dentro de la carpeta `GX-docs`, continúa con el **Paso 2** (instalar) según tu
sistema.

---

## Paso 2 (Windows 11) — Instalar

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

## Paso 2 (macOS / Linux) — Instalar

```bash
./install_global.sh           # instala/actualiza
./install_global.sh --dry-run # muestra qué haría
```

---

## Paso 3 (obligatorio) — Activar los hooks

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
