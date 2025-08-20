# Mihomo 规则集文件

本文件夹包含由四十九修改的网络 mihomo 配置规则集文件，用于网络流量的分类和路由。请勿用于非法用途。

## 文件说明

以下列出本目录中包含的所有规则集文件及其原始来源：

[ai.txt](./ai.txt) - 人工智能服务规则集

源文件链接: https://ruleset.skk.moe/Clash/non_ip/ai.txt

包含各种人工智能服务的域名规则，如 Google AI、OpenAI 等。

[AWAvenue.txt](./AWAvenue.txt) - 广告拦截规则集

源文件链接: https://github.com/TG-Twilight/AWAvenue-Ads-Rule/raw/refs/heads/main/Filters/AWAvenue-Ads-Rule-Clash-Classical.yaml

包含常见的广告域名，用于广告拦截。

[cdn.txt](./cdn.txt) - 内容分发网络域名规则集

源文件链接: https://ruleset.skk.moe/Clash/domainset/cdn.txt

包含各大内容分发网络(CDN)的域名后缀规则。

[cdn2.txt](./cdn2.txt) - 内容分发网络 IP 规则集

源文件链接: https://ruleset.skk.moe/Clash/non_ip/cdn.txt

包含各大内容分发网络(CDN)的域名后缀规则。

[cn.txt](./cn.txt) - 中国大陆 IP 段规则集

源文件链接: https://ruleset.skk.moe/Clash/ip/china_ip.txt 和 https://ruleset.skk.moe/Clash/ip/china_ip_ipv6.txt

包含中国大陆的 IP 地址段，用于识别和路由国内流量。

[tgip.txt](./tgip.txt) - Telegram IP 段规则集

源文件链接: https://core.telegram.org/resources/cidr.txt

包含 Telegram 服务的 IP 地址段，用于 Telegram 服务的专门路由。

## 注意事项

1. 请确保遵守相关法律法规，不要将这些规则用于非法用途

2. 规则集会定期更新，请关注源文件的更新情况

3. 根据实际需求选择合适的规则集，避免规则冲突
