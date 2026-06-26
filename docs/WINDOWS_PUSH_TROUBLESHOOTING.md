# WINDOWS_PUSH_TROUBLESHOOTING

## BATが壊れて実行される場合

`65001 is not recognized` や `it is not recognized` のようにコマンド先頭が欠ける場合は、BATの文字コード/改行解釈が壊れています。

このv6では `tools/PUSH_CLEAN_WINDOWS.bat` をASCII + CRLFに修正済みです。

PowerShellを使う場合:

```powershell
cd sales_os_clean_v6
powershell -ExecutionPolicy Bypass -File tools/PUSH_CLEAN_POWERSHELL.ps1
```

手動実行する場合:

```bat
cd sales_os_clean_v6
python tools\validate_sales_os.py
git init
git add -A
git commit -m "sales_os clean v5 audit ready structure"
git branch -M main
git remote remove origin
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
```
