Remove-Item "dist" -Recurse -Force
uv run dev\version-update.py
uv build

git add .
git commit -m "$(Get-Date -Format "yyyy-M-d_HH:mm:ss")"
git remote add origin git@github.com:Nine499/AI-49.git
git push
