# UUID 生成器（get-uuid）中文 README

## 📌 项目名称

**get-uuid - UUID Version 4 生成工具**

---

## 🧩 简介

这是一个基于 Python 的轻量级工具，用于快速生成符合 UUID Version 4 标准的唯一标识符，并提供自动复制到剪贴板功能。适用于开发调试、数据唯一性标识等场景。

---

## 🚀 核心功能

1. **自动生成 UUID Version 4**
   - 使用 `uuid.uuid4()` 算法生成 128 位随机唯一标识符
   - 标准格式：`xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`
2. **自动复制剪贴板**
   - 通过 `pyperclip` 库实现一键复制功能（跨平台兼容）
3. **终端可视化输出**
   - 在命令行界面显示生成的 UUID 并标注清晰前缀

---

## 🛠️ 环境依赖

| 依赖项    | 版本要求       | 安装方式                |
| --------- | -------------- | ----------------------- |
| Python    | 3.6+           | 系统自带/官方安装包     |
| pyperclip | 1.8.2+         | `pip install pyperclip` |
| uuid      | 标准库无需安装 | 内置模块无需额外操作    |

> 📝 **注意**：Windows 系统需确保已安装 `pywin32`，Linux 需安装 `xclip` 或 `xsel` 工具链

---

## 📦 安装指南

```bash
# 安装剪贴板依赖库
pip install pyperclip

# Linux 用户额外安装（任选其一）
sudo apt-get install xclip      # Debian/Ubuntu
sudo yum install xsel         # CentOS/RHEL
```

---

## 🧪 使用教程

### 方法一：直接运行脚本

```bash
# 执行生成操作
python get-uuid.py

# 输出示例
UUID: 123e4567-e89b-42d3-a456-556642440000
```

### 方法二：创建可执行文件（推荐）

```bash
# Linux/macOS 添加执行权限
chmod +x get-uuid.py

# 添加别名（建议写入 ~/.bashrc 或 ~/.zshrc）
alias getuuid="python /path/to/get-uuid.py"

# 使用别名快速调用
getuuid
```

---

## ⚠️ 注意事项

1. **剪贴板权限问题**
   - Linux 系统若报错 `PyperclipException`，请检查是否安装 `xclip/xsel`
   - Windows 系统需以管理员权限运行终端
2. **UUID 版本说明**
   - 当前仅支持 Version 4（随机生成），如需其他版本需修改 `uuid.uuid4()` 调用
3. **安全性提示**
   - 本工具生成的 UUID 不适用于加密安全场景（如密钥生成）

---

## 🤝 贡献指南

欢迎提交 Pull Request 或 Issue：

1. Fork 本仓库
2. 创建新分支 `feature/your-feature-name`
3. 提交代码并推送至远程分支
4. 创建合并请求

---

## 📄 许可证

MIT License
