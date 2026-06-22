Write-Host ""
Write-Host "Setting up radio-cli..." -ForegroundColor Cyan

# Create the virtual environment
Write-Host ""
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv .venv

# Upgrading pip
Write-Host "Upgrading internal installation tools..."
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
& ".\.venv\Scripts\pip.exe" install -e .

Write-Host ""
Write-Host "Done! To run the app, use:" -ForegroundColor Green
Write-Host "  .\launch.ps1" -ForegroundColor White
Write-Host ""
