# Python 工具集

这个目录包含了多个实用的 Python 脚本工具，每个工具都有特定的功能，用于解决各种日常任务和技术问题。

## 目录结构

```
python/
├── convert_html_entities_in_file/     # HTML实体转换工具
├── download_wenku8_novels/            # 下载轻小说工具
├── get_uuid/                          # UUID生成器
├── news_60s/                          # 每日60秒新闻获取工具
├── processing_cosplay_files/          # Cosplay文件处理工具
└── saoip/                             # IP地址扫描工具
```

## 工具详细介绍

### 1. convert_html_entities_in_file - HTML 实体转换工具

将 HTML 文件中的 HTML 实体转换为对应的字符。

#### 功能说明

- 将 HTML 实体如 `&amp;`、`&lt;`、`&gt;`、`&quot;` 等转换为对应的字符 `&`、`<`、`>`、`"` 等
- 支持 UTF-8 编码，能正确处理中文等特殊字符
- 包含完善的错误处理机制

#### 使用方法

```bash
python convert_html_entities_in_file.py <输入文件> <输出文件>
```

#### 示例

```bash
python convert_html_entities_in_file.py input.html output.html
```

### 2. download_wenku8_novels - 轻小说下载工具

从 wenku8 网站下载小说文件。

#### 功能说明

- 通过书籍 ID 从 wenku8 网站下载小说
- 自动清洗文件名中的非法字符
- 使用 cloudscraper 绕过网站的防护机制
- 包含完善的网络异常处理

#### 使用方法

```bash
# 通过命令行参数指定书籍ID
python download_wenku8_novels.py <书籍ID>

# 或者运行后输入书籍ID
python download_wenku8_novels.py
```

#### 示例

```bash
python download_wenku8_novels.py 1234
```

### 3. get_uuid - UUID 生成器

生成 UUIDv4 格式的唯一标识符，并复制到剪贴板。

#### 功能说明

- 生成基于随机数的 UUIDv4
- 自动将生成的 UUID 复制到系统剪贴板
- 包含剪贴板访问异常处理

#### 使用方法

```bash
python get_uuid.py
```

### 4. news_60s - 每日 60 秒新闻获取工具

从 60s.viki.moe 接口获取每日新闻，并以列表形式在控制台打印。

#### 功能说明

- 获取每日 60 秒读懂世界的新闻
- 以编号列表形式展示新闻内容
- 显示数据获取时间
- 包含完整的网络请求异常处理

#### 使用方法

```bash
python news_60s.py
```

### 5. processing_cosplay_files - Cosplay 文件处理工具

处理 cosplay 相关的文件，包含两个阶段的处理脚本。

#### 功能说明

**processing_cosplay_files1.py:**

- 解压指定目录下的所有压缩文件（zip, rar, 7z）
- 删除解压后的原压缩文件
- 删除指定目录下的所有.webp 和.gif 文件

**processing_cosplay_files2.py:**

- 删除指定目录下的所有非.webp 文件
- 删除所有空文件夹
- 将处理后的目录压缩为.7z 格式

#### 使用方法

```bash
# 第一阶段处理
python processing_cosplay_files1.py

# 第二阶段处理
python processing_cosplay_files2.py
```

> ⚠️ 注意：这些脚本会执行不可逆的操作，请确保已备份重要文件。

### 6. saoip - IP 地址扫描工具

扫描和测试 IP 地址连通性的工具，支持 ICMP 和 TCP 协议。

#### 功能说明

- 使用 ICMP 协议测试 IP 地址连通性 (ping)
- 使用 TCP 协议测试指定端口的连通性
- 支持 CIDR 格式的 IP 地址段扫描
- 多线程并发处理，提高扫描效率
- 输出连通的 IP 地址及响应时间

#### 使用方法

```bash
# ICMP测试单个IP
python saoip.py <IP地址>

# ICMP测试IP段
python saoip.py <IP段>

# TCP测试单个IP的指定端口
python saoip.py <IP地址> <端口列表>

# TCP测试IP段的指定端口
python saoip.py <IP段> <端口列表>
```

#### 示例

```bash
# 测试单个IP连通性
python saoip.py 192.168.1.1

# 测试IP段连通性
python saoip.py 192.168.1.1/24

# 测试单个IP的80端口
python saoip.py 192.168.1.1 80

# 测试IP段的80和443端口
python saoip.py 192.168.1.1/24 80,443

# 测试IP段的80-8080端口范围和443端口
python saoip.py 192.168.1.1/24 80,443,81-8080
```

## 通用说明

### 错误处理

所有脚本都包含完善的错误处理机制，能够处理网络异常、文件操作异常、权限异常等各种情况。

### 依赖项

部分脚本需要安装额外的 Python 包：

```bash
pip install cloudscraper  # download_wenku8_novels需要
pip install pyperclip     # get_uuid需要
pip install requests      # news_60s需要
```

### 系统要求

- Python 3.6+
- Windows/Linux/Mac OS
- 部分工具需要特定软件支持（如 7-Zip 用于处理压缩文件）

## 注意事项

1. 请在使用前仔细阅读每个工具的说明和使用方法
2. 某些工具会执行不可逆的操作，请确保已备份重要文件
3. 遵守相关法律法规，不要用于非法用途
4. 尊重网站的 robots.txt 和使用条款，合理使用网络资源
