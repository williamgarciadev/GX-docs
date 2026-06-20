<#
.SYNOPSIS
  Instala el grounding anti-alucinacion de GeneXus 18 de forma GLOBAL en Windows,
  para que los hooks de Claude Code corran en TODOS tus proyectos.

.DESCRIPTION
  1. Copia los hooks y el corpus a  %USERPROFILE%\.claude\genexus\
  2. Registra ambos hooks en tu settings de USUARIO  %USERPROFILE%\.claude\settings.json
     (UserPromptSubmit -> grounding ; PostToolUse Write|Edit -> validador),
     fusionando sin pisar lo que ya tengas.

  Los hooks resuelven el corpus en este orden:
    $env:GENEXUS_CORPUS_DIR  ->  %USERPROFILE%\.claude\genexus\corpus  ->  <proyecto>\corpus

.EXAMPLE
  ./install_global.ps1
  ./install_global.ps1 -DryRun

.NOTES
  Requiere Python 3 en el PATH. Idempotente: re-ejecutar actualiza sin duplicar.
  Si PowerShell bloquea el script:  powershell -ExecutionPolicy Bypass -File .\install_global.ps1
#>
param([switch]$DryRun)
$ErrorActionPreference = "Stop"

$SrcDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ConfigDir = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $env:USERPROFILE ".claude" }
$Dest = Join-Path $ConfigDir "genexus"
$Settings = Join-Path $ConfigDir "settings.json"

# Detectar el interprete de Python (python / python3 / py)
$Py = $null
foreach ($c in @("python", "python3", "py")) {
  if (Get-Command $c -ErrorAction SilentlyContinue) { $Py = $c; break }
}
if (-not $Py) {
  Write-Error "No encuentro Python en el PATH. Instala Python 3 (https://www.python.org/downloads/windows/) y reabre la terminal."
  exit 1
}

Write-Host "Origen  : $SrcDir"
Write-Host "Destino : $Dest"
Write-Host "Settings: $Settings"
Write-Host "Python  : $Py"
Write-Host ""

if (-not (Test-Path (Join-Path $SrcDir "corpus\api.tsv"))) {
  Write-Error "No encuentro corpus\api.tsv en $SrcDir. Ejecuta primero:  $Py build_corpus.py"
  exit 1
}

if ($DryRun) {
  Write-Host "[dry-run] Copiaria hooks  -> $Dest\hooks\"
  Write-Host "[dry-run] Copiaria corpus -> $Dest\corpus\"
  Write-Host "[dry-run] Fusionaria 2 hooks en $Settings"
  exit 0
}

# 1) Copiar hooks + corpus
New-Item -ItemType Directory -Force -Path (Join-Path $Dest "hooks")  | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $Dest "corpus") | Out-Null
Copy-Item (Join-Path $SrcDir ".claude\hooks\genexus_grounding.py") (Join-Path $Dest "hooks") -Force
Copy-Item (Join-Path $SrcDir ".claude\hooks\genexus_validate.py")  (Join-Path $Dest "hooks") -Force
Copy-Item (Join-Path $SrcDir "corpus\*") (Join-Path $Dest "corpus") -Recurse -Force
Write-Host "Copiados hooks y corpus a $Dest"

# 2) Construir los comandos del hook. En Windows NO se usa '|| true' (no existe
#    en cmd.exe); los hooks salen 0 normalmente, asi que no bloquean.
$gPath = Join-Path $Dest "hooks\genexus_grounding.py"
$vPath = Join-Path $Dest "hooks\genexus_validate.py"
$gCmd = "$Py `"$gPath`""
$vCmd = "$Py `"$vPath`""

# 3) Fusionar en settings.json con el script Python compartido
& $Py (Join-Path $SrcDir "tools\genexus_install_merge.py") $Settings $gCmd $vCmd

Write-Host ""
Write-Host "Listo. Abre Claude Code y ejecuta /hooks una vez (o reinicia) para que"
Write-Host "cargue los hooks globales. A partir de ahi corren en CUALQUIER proyecto."
