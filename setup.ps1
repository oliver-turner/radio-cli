$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "Setting up radio-cli..." -ForegroundColor Cyan

if (-not (Get-Command uv -ErrorAction SilentlyContinue))
{
    Write-Host ""
    Write-Host "uv not found. Installing from official Astral source..." -ForegroundColor Yellow
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
}

Write-Host ""
Write-Host "Syncing dependencies from uv.lock (hash-verified)..." -ForegroundColor Yellow

uv sync --frozen

if ($LASTEXITCODE -ne 0)
{
    Write-Host ""
    Write-Host "ERROR: uv sync failed. Lockfile may be out of date or tampered with." -ForegroundColor Red
    Write-Host "If you intentionally changed pyproject.toml, run: uv lock" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Done! All dependencies installed from verified hashes." -ForegroundColor Green
Write-Host "To run the app, use:" -ForegroundColor Green
Write-Host "  .\launch.ps1" -ForegroundColor White
Write-Host ""
