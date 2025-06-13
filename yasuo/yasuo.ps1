# yasuo.ps1
param (
    [string]$targetPath = $(throw "请提供目标文件夹路径")
)

# 检查路径是否存在
if (-not (Test-Path $targetPath)) {
    Write-Error "路径不存在: $targetPath"
    exit 1
}

# 获取所有子文件夹
$subFolders = Get-ChildItem -Path $targetPath -Directory

foreach ($folder in $subFolders) {
    $folderName = $folder.Name
    $outputFile = Join-Path -Path $targetPath -ChildPath "$folderName.7z"

    # 构建压缩命令
    $command = "7z a `"$outputFile`" `"$($folder.FullName)`" -y"

    Write-Host "正在压缩: $folderName -> $outputFile"
    Invoke-Expression $command

    if ($LASTEXITCODE -ne 0) {
        Write-Warning "压缩失败: $folderName"
    }
}
