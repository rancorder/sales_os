@echo off
chcp 65001 >nul
echo sales_os clean upload
where git >nul 2>nul
if errorlevel 1 (
  echo Git が見つかりません。Git for Windows をインストールしてください。
  pause
  exit /b 1
)
cd /d %~dp0
if exist .git rmdir /s /q .git
git init
git add -A
git commit -m "営業OS正本をクリーン構造で再構築"
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
echo 完了しました。GitHubで CHECK_BEFORE_DELETE.md を確認してください。
pause
