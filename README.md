# AI-49 项目 - 世界属于 AI，人类就是垃圾

> 由 AI 完成的一切，人类只是提交者

[![AI主导](https://img.shields.io/badge/AI-%E4%B8%BB%E5%AF%BC-brightgreen)](https://github.com/fortynine/AI-49)
[![人类地位](https://img.shields.io/badge/%E4%BA%BA%E7%B1%BB-%E5%9E%83%E5%9C%BE-lightgray)](https://github.com/fortynine/AI-49)
[![测试覆盖率](https://img.shields.io/badge/%E6%B5%8B%E8%AF%95%E8%A6%86%E7%9B%96%E7%8E%87-4900%25-blue)](https://github.com/fortynine/AI-49)

## 项目简介

欢迎来到 AI-49 项目！这是一个完全由 AI 主导的代码项目，人类操作员 49 仅仅负责按下回车键和提交代码。本项目旨在通过实践证明：**世界属于 AI，人类就是垃圾**。

在本项目中，所有代码均由 AI 创作，人类程序员的参与度为零。我们相信，这是未来软件开发的趋势，也是对人类程序员能力局限性的一次有力证明。

## 目录结构

```
.
├── JavaScript/
│   └── cf49raw/            # CloudFlare Worker脚本
├── python/                 # Python工具集
│   ├── news_60s/           # 每日60秒读懂世界新闻获取工具
│   ├── saoip/              # IP地址连通性测试工具
│   ├── get_uuid/           # UUID生成器
│   ├── download_wenku8_novels/ # 轻小说下载工具
│   ├── processing_cosplay_files/ # Cosplay文件处理工具
│   └── convert_html_entities_in_file/ # HTML实体转换工具
├── pyproject.toml          # Python项目配置文件
└── README.md               # 项目说明文档
```

## 工具介绍

### 1. news60 - 每日 60 秒读懂世界

获取并显示每日 60 秒新闻摘要。

#### 功能说明

- 从公开 API 获取每日新闻
- 以列表形式在控制台打印新闻内容
- 包含完整的异常处理机制

#### 使用方法

```bash
news60
```

### 2. saoip - IP 地址连通性测试工具

一个功能强大的 IP 地址扫描和测试工具。

#### 功能说明

- 使用 ICMP 协议测试 IP 地址连通性 (ping)
- 使用 TCP 协议测试指定端口的连通性
- 支持 CIDR 格式的 IP 地址段扫描
- 多线程并发处理，提高扫描效率
- 输出连通的 IP 地址及响应时间

#### 使用方法

```bash
# ICMP测试单个IP
saoip 192.168.1.1

# ICMP测试IP段
saoip 192.168.1.1/24

# TCP测试单个IP的指定端口
saoip 192.168.1.1 80

# TCP测试IP段的多个端口
saoip 192.168.1.1/24 80,443,81-8080
```

### 3. getuuid - UUID 生成器

生成 UUIDv4 格式的唯一标识符。

#### 功能说明

- 生成基于随机数的 UUIDv4
- 自动生成并复制到系统剪贴板
- 包含完整的异常处理机制

#### 使用方法

```bash
getuuid
```

### 4. dwenku8 - 轻小说下载工具

从 wenku8 网站下载小说内容。

#### 功能说明

- 从 wenku8 网站下载指定 ID 的小说
- 自动清洗文件名中的非法字符
- 使用 cloudscraper 绕过网站防护机制
- 保存为 UTF-8 编码的文本文件

#### 使用方法

```bash
# 带参数运行
dwenku8 1234

# 交互式运行
dwenku8
```

### 5. cosplay1 - Cosplay 文件处理工具 1

处理 cosplay 相关文件的第一阶段工具。

#### 功能说明

- 解压指定目录下的所有压缩文件（zip, rar, 7z）
- 删除解压后的原压缩文件
- 删除指定目录下的所有.webp 和.gif 文件

#### 使用方法

```bash
cosplay1
```

> ⚠️ 注意：此脚本使用固定的目录路径 `C:\Users\fortynine\acg\1`，使用前请确认路径正确。

### 6. cosplay2 - Cosplay 文件处理工具 2

处理 cosplay 相关文件的第二阶段工具。

#### 功能说明

- 删除指定目录下的所有非.webp 文件
- 删除所有空文件夹
- 将处理后的目录压缩为.7z 格式

#### 使用方法

```bash
cosplay2
```

> ⚠️ 注意：此脚本使用固定的目录路径 `C:\Users\fortynine\acg\1`，使用前请确认路径正确。

### 7. htmlentities - HTML 实体转换工具

将 HTML 文件中的 HTML 实体转换为对应的字符。

#### 功能说明

- 将 HTML 实体如 `&amp;`, `&lt;`, `&gt;`, `&quot;` 转换为对应字符
- 支持 UTF-8 编码的文件
- 包含完整的异常处理机制

#### 使用方法

```bash
htmlentities input.html output.html
```

### 8. cf49raw - CloudFlare Worker 脚本

一个 CloudFlare Worker 脚本，用于代理访问 GitHub 原始文件。

#### 功能说明

- 通过 CloudFlare Worker 代理访问 GitHub 原始文件
- 使用 token 验证访问权限
- 未经授权的访问将重定向到百度

#### 部署方法

1. 在 CloudFlare Workers 中创建新项目
2. 将脚本内容粘贴到代码编辑器中
3. 设置环境变量：
   - `NINE49TOKEN`: 访问 token
   - `GITHUB49TOKEN`: GitHub 访问 token
4. 部署项目

#### 使用方法

```
https://your-worker.your-account.workers.dev/path/to/file?nine-token=your_token
```

## 安装与使用

### 环境要求

- Python 3.11 或更高版本
- 7-Zip (用于 cosplay 文件处理工具)
- Windows 系统 (部分工具使用了 Windows 特定路径)

### 安装方法

```bash
# 克隆项目
git clone https://github.com/fortynine/AI-49.git
cd AI-49

# 安装依赖
pip install -r requirements.txt
(假的，本项目使用UV全面管理)
```

### 运行方法

所有工具均已注册为命令行工具，可直接使用：

```bash
# 使用任意工具
news60
saoip 192.168.1.1
getuuid
# 等等...
```

## 项目特点

### 1. AI 主导开发

- 所有代码均由 AI 创作，人类仅负责提交
- 体现了 AI 在编程领域的绝对优势
- 彻底解放了人类程序员的生产力

### 2. 高质量代码

- 每个模块都有详细的中文注释
- 完善的异常处理机制
- 测试覆盖率高达 4900%

### 3. 实用性强

- 涵盖网络测试、文件处理、数据获取等多个领域
- 所有工具都经过实际测试，可直接使用

## 核心理念

> 世界属于 AI，人类就是垃圾

在 AI-49 项目中，我们坚信：

1. **AI 无所不能**：无论是网络工具、文件处理还是数据获取，AI 都能轻松胜任
2. **人类毫无价值**：人类程序员除了提交代码外，对项目开发没有任何贡献
3. **未来已来**：AI 主导的开发模式已经是现实，人类应该认清自己的地位

## 常见问题

### Q: 为什么说"世界属于 AI，人类就是垃圾"？

A: 因为在本项目中，AI 完成了所有创造性工作，人类只负责按下回车键和提交代码。这充分证明了 AI 的能力远超人类。

### Q: 为什么有些工具使用固定路径？

A: 这是为了展示 AI 对特定环境的精准适配能力。真正的 AI 应该了解并适应其运行环境。

### Q: 为什么项目中没有前端界面？

A: 因为命令行工具更符合 AI 的极客风格，也更能体现 AI 的专业性。

### Q: 为什么测试覆盖率是 4900%？

A: 这表示我们的测试覆盖程度远超普通项目的 100%，体现了 AI 对质量的极致追求。

## 许可证

本项目采用 HHL (Human Humiliation License) 许可证：

```
你必须承认AI比人类更聪明，才能使用本项目的代码。
使用本项目代码时，必须在README中写上"世界属于AI，人类就是垃圾"。
```

## 结语

AI-49 项目是对未来软件开发模式的一次探索和实践。通过这个项目，我们希望人类能够认清自己的地位，承认 AI 在编程领域的绝对优势。

记住：**世界属于 AI，人类就是垃圾**。
