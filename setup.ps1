Write-Host ""
Write-Host "Setting up radio-cli..." -ForegroundColor Cyan

# Create the virtual environment
Write-Host ""
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv .venv

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
& ".\.venv\Scripts\pip.exe" install -e .

Write-Host ""
Write-Host "Done! To run the app, use:" -ForegroundColor Green
Write-Host "  .\launch.ps1" -ForegroundColor White
Write-Host ""
