echo 下载规则
mkdir -p mihomo/tmp
curl -fsSL -o mihomo/tmp/cnipv4.txt https://ruleset.skk.moe/Clash/ip/china_ip.txt
curl -fsSL -o mihomo/tmp/cnipv6.txt https://ruleset.skk.moe/Clash/ip/china_ip_ipv6.txt
curl -fsSL -o mihomo/tmp/tgip.txt https://core.telegram.org/resources/cidr.txt
curl -fsSL -o mihomo/tmp/AWAvenue.txt https://github.com/TG-Twilight/AWAvenue-Ads-Rule/raw/refs/heads/main/Filters/AWAvenue-Ads-Rule-Clash-Classical.yaml
curl -fsSL -o mihomo/tmp/cdn.txt https://ruleset.skk.moe/Clash/domainset/cdn.txt
curl -fsSL -o mihomo/tmp/cdn2.txt https://ruleset.skk.moe/Clash/non_ip/cdn.txt
curl -fsSL -o mihomo/tmp/ai.txt https://ruleset.skk.moe/Clash/non_ip/ai.txt
