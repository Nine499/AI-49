echo 提交并推送更新
git config --local user.email "deceit-bucket-shy@duck.com"
git config --local user.name "Nine_Action_bot"
find mihomo -maxdepth 1 -name "*.txt" -exec git add {} +
if ! git diff --cached --quiet; then
    git commit -m "🤖 自动更新规则 $(TZ='Asia/Shanghai' date '+%Y-%m-%d %H:%M:%S')"
    git push
fi
