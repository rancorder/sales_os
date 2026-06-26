$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "[1/7] Validate sales_os..."
python tools/validate_sales_os.py

Write-Host "[2/7] Initialize git..."
git init

Write-Host "[3/7] Stage files..."
git add -A

Write-Host "[4/7] Commit files..."
git commit -m "sales_os clean v5 audit ready structure"
if ($LASTEXITCODE -ne 0) {
  Write-Host "No changes to commit or commit failed. Continuing to branch/remote setup..."
}

Write-Host "[5/7] Set main branch..."
git branch -M main

Write-Host "[6/7] Reset origin..."
git remote remove origin 2>$null
git remote add origin https://github.com/rancorder/sales_os.git

Write-Host "[7/7] Force push to GitHub..."
git push -f origin main

Write-Host "Done. sales_os was pushed successfully."
Read-Host "Press Enter to exit"
