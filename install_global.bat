@echo off
REM ============================================================
REM  Doble clic para instalar el grounding GeneXus de forma
REM  GLOBAL en Windows (Claude Code CLI).
REM  Lanza install_global.ps1 saltando la politica de ejecucion
REM  de PowerShell. No requiere permisos de administrador.
REM ============================================================
setlocal
cd /d "%~dp0"

echo ============================================================
echo  Instalador GLOBAL del grounding GeneXus (Claude Code)
echo ============================================================
echo.

REM Preferir PowerShell 7 (pwsh) si esta; si no, el PowerShell de Windows.
where pwsh >nul 2>nul
if %ERRORLEVEL%==0 (
  pwsh -NoProfile -ExecutionPolicy Bypass -File "%~dp0install_global.ps1"
) else (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install_global.ps1"
)

echo.
echo ============================================================
echo  Si no hubo errores arriba: abre Claude Code y ejecuta /hooks
echo  una vez (o reinicia la CLI) para activar los hooks globales.
echo ============================================================
echo.
pause
