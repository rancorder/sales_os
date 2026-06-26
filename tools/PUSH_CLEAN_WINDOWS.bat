@echo off
setlocal
cd /d "%~dp0\.."

echo [1/7] Validate sales_os...
python tools\validate_sales_os.py
if errorlevel 1 (
  echo Validation failed. Stop.
  pause
  exit /b 1
)

echo [2/7] Initialize git...
git init
if errorlevel 1 goto git_error

echo [3/7] Stage files...
git add -A
if errorlevel 1 goto git_error

echo [4/7] Commit files...
git commit -m "sales_os clean v6 audit ready structure"
if errorlevel 1 (
  echo No changes to commit or commit failed. Continuing to branch setup...
)

echo [5/7] Set main branch...
git branch -M main
if errorlevel 1 goto git_error

echo [6/7] Reset origin...
git remote remove origin 2>nul
git remote add origin https://github.com/rancorder/sales_os.git
if errorlevel 1 goto git_error

echo [7/7] Force push to GitHub...
git push -f origin main
if errorlevel 1 goto git_error

echo Done. sales_os was pushed successfully.
pause
exit /b 0

:git_error
echo Git command failed. Make sure Git is installed and you are logged in.
pause
exit /b 1
