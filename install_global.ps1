<#
.SYNOPSIS
  Instala el grounding anti-alucinacion de GeneXus 18 de forma GLOBAL en Windows,
  para que los hooks de Claude Code corran en TODOS tus proyectos.

.DESCRIPTION
  1. Copia los hooks y el corpus GeneXus a  %USERPROFILE%\.claude\genexus\
     y, si existe, tambien corpus_bantotal\ (Bantotal es opcional)
  2. Registra ambos hooks en tu settings de USUARIO  %USERPROFILE%\.claude\settings.json
     (UserPromptSubmit -> grounding ; PostToolUse Write|Edit -> validador),
     fusionando sin pisar lo que ya tengas.

  Los hooks resuelven cada corpus en este orden:
    $env:GENEXUS_CORPUS_DIR   -> %USERPROFILE%\.claude\genexus\corpus          -> <proyecto>\corpus
    $env:BANTOTAL_CORPUS_DIR  -> %USERPROFILE%\.claude\genexus\corpus_bantotal -> <proyecto>\corpus_bantotal

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

$HasBantotal = Test-Path (Join-Path $SrcDir "corpus_bantotal\tables.tsv")

if ($DryRun) {
  Write-Host "[dry-run] Copiaria hooks  -> $Dest\hooks\"
  Write-Host "[dry-run] Copiaria corpus -> $Dest\corpus\"
  if ($HasBantotal) {
    Write-Host "[dry-run] Copiaria corpus_bantotal -> $Dest\corpus_bantotal\"
  } else {
    Write-Host "[dry-run] corpus_bantotal\ no encontrado, se omite (opcional)"
  }
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

# 1b) Corpus Bantotal, si esta presente (opcional)
if ($HasBantotal) {
  New-Item -ItemType Directory -Force -Path (Join-Path $Dest "corpus_bantotal") | Out-Null
  Copy-Item (Join-Path $SrcDir "corpus_bantotal\*") (Join-Path $Dest "corpus_bantotal") -Recurse -Force
  Write-Host "Copiado corpus_bantotal a $Dest\corpus_bantotal"
} else {
  Write-Host "corpus_bantotal\ no encontrado en $SrcDir, se omite (opcional)"
}

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
