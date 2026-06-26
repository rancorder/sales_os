#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 tools/validate_sales_os.py
git init
git add -A
git commit -m "営業OS正本 v4: Drive ID増加対応テーブルへ更新"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
