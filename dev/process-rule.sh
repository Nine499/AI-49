echo 处理规则
# 处理 mihomo/tmp/cnipv4.txt 和 mihomo/tmp/cnipv6.txt
# 要求：删除包含#的行，删除空行，在每行开头添加IP-CIDR,，合并到 mihomo/cn.txt
cat mihomo/tmp/cnipv4.txt mihomo/tmp/cnipv6.txt | grep -v '#' | grep -v '^$' | sed 's/^/IP-CIDR,/' > mihomo/cn.txt
# 处理 mihomo/tmp/tgip.txt
# 要求：删除包含#的行，删除空行，在每行开头添加IP-CIDR,，输出为 mihomo/tgip.txt
grep -v '#' mihomo/tmp/tgip.txt | grep -v '^$' | sed 's/^/IP-CIDR,/' > mihomo/tgip.txt
# 处理 mihomo/tmp/AWAvenue.txt
# 要求：删除包含#的行，删除包含payload的行，删除空行，将`  - DOMAIN`替换为`DOMAIN`，输出为 mihomo/AWAvenue.txt
grep -v '#' mihomo/tmp/AWAvenue.txt | grep -v 'payload' | grep -v '^$' | sed 's/  - DOMAIN/DOMAIN/' > mihomo/AWAvenue.txt
# 处理 mihomo/tmp/cdn.txt
# 要求：删除包含#的行，如果开头有+.则删除+.，删除空行，在每行开头添加DOMAIN-SUFFIX
# 处理 mihomo/tmp/cdn2.txt
# 要求：删除包含#的行，删除空行
# 输出为 mihomo/cdn.txt
grep -v '^#' mihomo/tmp/cdn.txt | sed 's/^+\.*//' | awk 'NF' | sed 's/^/DOMAIN-SUFFIX,/' > mihomo/cdn.txt && grep -v '^#' mihomo/tmp/cdn2.txt | awk 'NF' >> mihomo/cdn.txt
# 处理 mihomo/tmp/ai.txt
# 要求：删除包含#的行，删除空行，输出为 mihomo/ai.txt
grep -v '#' mihomo/tmp/ai.txt | grep -v '^$' > mihomo/ai.txt
# 标注行数
find mihomo -maxdepth 1 -name "*.txt" -exec sh -c 'file="{}"; [ -f "$file" ] || exit 0; first_line=$(head -n 1 "$file"); if echo "$first_line" | grep -q "^# 本文件共有 [0-9]* 行$"; then echo "跳过 $file (已处理)"; else line_count=$(wc -l < "$file"); temp_file=$(mktemp); echo "# 本文件共有 $line_count 行" > "$temp_file"; cat "$file" >> "$temp_file"; mv "$temp_file" "$file"; echo "已处理 $file"; fi' \;
