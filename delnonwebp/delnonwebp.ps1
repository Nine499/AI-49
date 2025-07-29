# 定义目标路径
$targetDir = "C:\Users\fortynine\acg\1"

# 删除非 .webp 文件
Get-ChildItem -Path $targetDir -Recurse -File | Where-Object {
    $_.Extension.ToLower() -ne ".webp"
} | ForEach-Object {
    # 使用 -LiteralPath 避免特殊字符问题
    Remove-Item -LiteralPath $_.FullName -Force
}

# 删除空文件夹（从深层到父级）
Get-ChildItem -Path $targetDir -Recurse -Directory | Sort-Object FullName -Descending | ForEach-Object {
    # 检查文件夹是否为空（包含隐藏/系统文件）
    if ((Get-ChildItem -LiteralPath $_.FullName -Force | Measure-Object).Count -eq 0) {
        Remove-Item -LiteralPath $_.FullName -Force
    }
}
