Remove-Item "dist" -Recurse -Force
uv run dev\version-update.py
uv build
