function ico49 {
    param(
        [Parameter(Mandatory=$true)]
        [string]$domain,

        [int]$size = 256
    )

    # URL 编码处理
    $encodedDomain = [uri]::EscapeDataString("http://$domain")
    # 动态生成 URL
    $url = "https://t0.gstatic.cn/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=$encodedDomain&size=$size"
    # 生成文件名
    $fileName = "$domain.ico"

    # 修复下载路径获取方式（使用环境变量替代.NET方法）
    $downloadPath = "$env:USERPROFILE\Downloads"
    $filePath = Join-Path $downloadPath $fileName

    try {
        # 添加调试信息输出
        Write-Host "下载路径: $filePath"
        Write-Host "请求地址: $url"

        # 下载文件（使用更兼容的下载方式）
        $webClient = New-Object System.Net.WebClient
        $webClient.Headers.Add("User-Agent", "PowerShell Script")
        $webClient.DownloadFile($url, $filePath)
        Write-Host "图标已保存到 $filePath" -ForegroundColor Green
    } catch {
        Write-Host "下载失败: $_" -ForegroundColor Red
        Write-Host "错误详情: $($Error[0].Exception.Message)" -ForegroundColor Yellow
    }
}

