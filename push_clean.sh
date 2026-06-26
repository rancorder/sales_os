#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
rm -rf .git
git init
git add -A
git commit -m "営業OS正本をクリーン構造で再構築"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
echo "Done. Check CHECK_BEFORE_DELETE.md on GitHub."
