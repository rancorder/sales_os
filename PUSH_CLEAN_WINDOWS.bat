@echo off
chcp 65001
cd /d %~dp0
python toolsalidate_sales_os.py
if errorlevel 1 (
  echo Validation failed. Stop.
  pause
  exit /b 1
)
git init
git add -A
git commit -m "営業OS正本 v4: Drive ID増加対応テーブルへ更新"
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
pause
