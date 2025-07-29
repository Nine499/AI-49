# dns49
function dns49 {
    param (
        [string]$domain = "qq.com",
        [string]$record = "A"
    )

    $servers = @{
        "阿里"         = "223.5.5.5"
        "阿里 DOH"     = "https://dns.alidns.com/dns-query"
        "腾讯"         = "119.29.29.29"
        "腾讯 DOH"     = "https://doh.pub/dns-query"
        "Clash"        = "127.0.0.1:4953"
        "谷歌 DOH"     = "https://dns.google/dns-query"
    }

    foreach ($name in $servers.Keys) {
        Write-Host "$name："
        qdns $record $domain -s $servers[$name]
        Write-Host ""
    }
}
