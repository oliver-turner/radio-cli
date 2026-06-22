$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $root
try
{
    uv run --frozen python main.py
} finally
{
    Pop-Location
}
