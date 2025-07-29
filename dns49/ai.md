windows WindowsPowerShell\profile.ps1 增加代码要求如下

执行 dns49 qq.com a
代码返回
阿里：
qdns a qq.com -s 223.5.5.5 的结果
阿里 DOH：
qdns a qq.com -s https://dns.alidns.com/dns-query 的结果
腾讯：
qdns a qq.com -s 119.29.29.29 的结果
腾讯 DOH：
qdns a qq.com -s https://doh.pub/dns-query 的结果
Clash：
qdns a qq.com -s 127.0.0.1:4953 的结果
谷歌 DOH：
qdns a qq.com -s https://dns.google/dns-query 的结果

qq.com 或者 a 都是变量，用户可以随意输入或者不输入
