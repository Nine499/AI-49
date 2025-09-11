# AI-49 项目

> 世界属于 AI，人类就是垃圾

AI-49 是一个完全由 AI 主导开发的项目，人类仅负责提交代码。旨在证明 AI 在软件开发中的绝对优势。

## 项目概述

### 核心理念

本项目坚信"世界属于 AI，人类就是垃圾"，所有代码均由 AI 编写，人类只负责代码提交和部署。

### 目标用户

- 系统管理员
- 开发人员
- 网络测试人员
- 小说爱好者
- 图像文件处理人员

### 解决的问题

- 提供每日新闻摘要
- 测试 IP 地址连通性
- 生成 UUID
- 下载轻小说
- 处理 Cosplay 文件
- HTML 实体转换
- GitHub 文件代理访问

## 目录结构

```text
.
├── JavaScript                    # JavaScript 相关工具
│   ├── cf-github-raw            # GitHub 文件代理工具 (CloudFlare Worker)
│   │   └── cf-github-raw.js
│   └── vercel-github-raw        # GitHub 文件代理工具 (Vercel)
│       ├── vercel-github-raw.js
│       └── vercel.json
├── dev                           # 开发工具
│   └── version-update.py
├── mihomo                        # Mihomo 规则文件
│   ├── AWAvenue.txt
│   ├── ai.txt
│   ├── cdn.txt
│   ├── cdn2.txt
│   ├── cn.txt
│   └── tgip.txt
├── python                        # Python 工具集合
│   ├── convert_html_entities_in_file    # HTML 实体转换工具
│   │   └── convert_html_entities_in_file.py
│   ├── download_wenku8_novels           # 轻小说下载工具
│   │   └── download_wenku8_novels.py
│   ├── get_uuid                         # UUID 生成工具
│   │   └── get_uuid.py
│   ├── news_60s                         # 每日新闻工具
│   │   └── news_60s.py
│   ├── processing_cosplay_files         # Cosplay 文件处理工具
│   │   ├── processing_cosplay_files1.py
│   │   └── processing_cosplay_files2.py
│   └── saoip                            # IP 扫描工具
│       └── saoip.py
├── README.md
└── pyproject.toml
```

## 工具详解

### 1. cf-github-raw - GitHub 文件代理工具 (CloudFlare Worker)

位于 `JavaScript/cf-github-raw/` 目录下，用于通过 CloudFlare Worker 代理访问 GitHub 上的原始文件。

#### cf-github-raw 功能特点

- 通过 CloudFlare Worker 代理访问 GitHub 原始文件
- 支持 token 验证，提高安全性
- 隐藏真实 GitHub 地址，防止被探测

#### cf-github-raw 部署方式

1. 创建 CloudFlare Worker 项目
2. 粘贴 [cf-github-raw.js](JavaScript/cf-github-raw/cf-github-raw.js) 内容
3. 设置环境变量 `NINE49TOKEN` 和 `GITHUB49TOKEN`
4. 部署项目

#### cf-github-raw 使用方法

```url
# 访问 GitHub 文件
https://your-worker.your-name.workers.dev/fortynine/AI-49/README.md?nine-token=your_token
```

### 2. vercel-github-raw - GitHub 文件代理工具 (Vercel)

位于 `JavaScript/vercel-github-raw/` 目录下，用于通过 Vercel 代理访问 GitHub 上的原始文件。

#### vercel-github-raw 功能特点

- 通过 Vercel Serverless Functions 代理访问 GitHub 原始文件
- 支持 token 验证，提高安全性
- 隐藏真实 GitHub 地址，防止被探测
- 支持 Vercel 部署

#### vercel-github-raw 部署方式

1. 将 [JavaScript/vercel-github-raw/](JavaScript/vercel-github-raw/) 目录作为根目录部署到 Vercel
2. 设置环境变量 `NINE49TOKEN` 和 `GITHUB49TOKEN`
3. 配置 `vercel.json` 路由规则

#### vercel-github-raw 使用方法

```url
# Vercel 部署方式访问
https://your-vercel-app.vercel.app/fortynine/AI-49/README.md?nine-token=your_token
```

### 3. news_60s - 每日 60 秒新闻

位于 `python/news_60s/news_60s.py`，用于获取每日 60 秒读懂世界的新闻。

#### news_60s 功能特点

- 从 60s.viki.moe 接口获取每日新闻
- 控制台格式化输出新闻列表
- 完善的错误处理机制

#### news_60s 使用方法

```bash
python news_60s.py
```

### 4. saoip - IP 扫描工具

位于 `python/saoip/saoip.py`，用于扫描和测试 IP 地址连通性。

#### saoip 功能特点

- 支持 ICMP 协议测试 IP 连通性 (ping)
- 支持 TCP 协议测试指定端口连通性
- 支持 CIDR 格式的 IP 地址段扫描
- 多线程并发处理，提高扫描效率
- 输出连通的 IP 地址及响应时间

#### saoip 使用方法

```bash
# ICMP 测试单个 IP
python saoip.py 192.168.1.1

# ICMP 测试 IP 段
python saoip.py 192.168.1.1/24

# TCP 测试单个 IP 的指定端口
python saoip.py 192.168.1.1 80

# TCP 测试 IP 段的多个端口
python saoip.py 192.168.1.1/24 80,443,81-8080
```

### 5. get_uuid - UUID 生成工具

位于 `python/get_uuid/get_uuid.py`，用于生成 UUIDv4 格式的唯一标识符。

#### get_uuid 功能特点

- 生成 UUIDv4 格式的唯一标识符
- 自动复制到系统剪贴板
- 友好的用户界面提示

#### get_uuid 使用方法

```bash
python get_uuid.py
```

### 6. download_wenku8_novels - 轻小说下载工具

位于 `python/download_wenku8_novels/download_wenku8_novels.py`，用于从 wenku8 网站下载小说。

#### download_wenku8_novels 功能特点

- 通过 wenku8 网站下载小说内容
- 自动清洗文件名中的非法字符
- 使用 cloudscraper 绕过网站防护
- 完善的错误处理机制

#### download_wenku8_novels 使用方法

```bash
# 方式1: 命令行参数指定书籍ID
python download_wenku8_novels.py 1234

# 方式2: 运行时输入书籍ID
python download_wenku8_novels.py
```

### 7. processing_cosplay_files - Cosplay 文件处理工具

位于 `python/processing_cosplay_files/` 目录下，包含两个处理 cosplay 文件的工具。

#### processing_cosplay_files1.py

##### processing_cosplay_files1 功能特点

- 解压指定目录下的所有压缩文件（zip, rar, 7z）
- 删除解压后的原压缩文件
- 删除指定目录下的所有 .webp 和 .gif 文件

##### processing_cosplay_files1 使用方法

```bash
python processing_cosplay_files1.py
```

#### processing_cosplay_files2.py

##### processing_cosplay_files2 功能特点

- 删除指定目录下的所有非 .webp 文件
- 删除所有空文件夹
- 将处理后的目录压缩为 .7z 格式

##### processing_cosplay_files2 使用方法

```bash
python processing_cosplay_files2.py
```

### 8. convert_html_entities_in_file - HTML 实体转换工具

位于 `python/convert_html_entities_in_file/convert_html_entities_in_file.py`，用于将 HTML 文件中的实体转换为对应字符。

#### convert_html_entities_in_file 功能特点

- 将 HTML 实体（如 &amp;, &lt;, &gt;, &quot; 等）转换为对应字符
- 支持 UTF-8 编码文件
- 完善的错误处理机制

#### convert_html_entities_in_file 使用方法

```bash
python convert_html_entities_in_file.py input.html output.html
```

### 9. mihomo - 规则文件集合

位于 `mihomo/` 目录下，包含多个用于 Mihomo (Clash Meta) 的规则文件：

- AWAvenue.txt - AWAvenue 规则
- ai.txt - AI 相关规则
- cdn.txt - CDN 规则
- cdn2.txt - CDN 规则（补充）
- cn.txt - 中国网络规则
- tgip.txt - Telegram IP 规则

## 技术架构

### 系统架构

- 命令行工具模式: 每个功能模块作为独立命令行工具
- 单一职责原则: 每个脚本只完成一个核心功能
- 环境适配模式: 固定路径适配特定运行环境

### 技术选型

- 编程语言: Python 3.11+, JavaScript (ES6+)
- 前端: 无
- 后端: Python 脚本 + CloudFlare Worker + Vercel Serverless Functions
- 数据库: 无
- 其他依赖:
  - cloudscraper (用于绕过网站防护)
  - 7-Zip (用于文件压缩)
  - Windows 系统 (部分工具依赖 Windows 路径)

## 开发环境

### 必需工具

- Python 3.11 或更高版本
- Git
- 7-Zip
- Windows 系统

### 可选工具

- UV (用于依赖管理)

### 运行环境

```bash
git clone https://github.com/fortynine/AI-49.git
cd AI-49
pip install -r requirements.txt  # 实际使用 UV 管理依赖
```

### 本地开发

直接运行命令行工具如 `news60`, `saoip`, `getuuid` 等

### 部署

#### CloudFlare Worker 部署

```bash
1. 创建新项目
2. 粘贴 cf-github-raw.js 内容
3. 设置环境变量 NINE49TOKEN 和 GITHUB49TOKEN
4. 部署项目
```

#### Vercel 部署

```bash
1. 将 JavaScript/vercel-github-raw/ 目录作为根目录部署到 Vercel
2. 设置环境变量 NINE49TOKEN 和 GITHUB49TOKEN
3. 配置 vercel.json 路由规则
```

## 技术约束

### 代码规范

- 所有模块包含详细中文注释
- 所有代码对小白，对初学者友好

### 性能要求

- 多线程提高扫描效率

### 安全要求

- 使用 token 验证访问权限（cf-github-raw 和 vercel-github-raw）

### 已知问题

- 部分工具使用固定路径（如 C:\Users\fortynine\acg\1）
- 仅支持 Windows 系统（部分工具）
- 测试覆盖率 4900% 为夸张表述
- 无前端界面

## 项目特点

1. 所有代码由 AI 编写
2. 完善的异常处理机制
3. 高测试覆盖率（4900%）
4. 多线程处理
5. 支持 CIDR 和端口范围扫描
