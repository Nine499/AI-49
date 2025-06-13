# SAOIP 端口扫描工具

## 项目简介

SAOIP（Simple Asynchronous Open IP Port Scanner）是一款轻量级的网络端口扫描工具，采用 Python 编写，支持多线程并发扫描。该工具可检测指定 IP 地址（或 IP 段）的多个端口开放状态，并计算连接延迟时间。

## 功能特性

- **并发扫描**：使用`ThreadPoolExecutor`实现 100 线程并发扫描
- **智能 IP 解析**：支持 CIDR 格式 IP 段（如 192.168.1.0/24）和单 IP 混合扫描
- **超时控制**：1 秒超时机制防止长时间阻塞
- **错误处理**：
  - 自动捕获超时（`socket.timeout`）
  - 自动捕获连接拒绝（`ConnectionRefusedError`）
  - 异常错误信息捕获
- **结果展示**：输出格式为`IP地址 端口号 延迟时间`

## 使用方法

### 命令格式

```bash
python saoip.py <ip_range> <port1> <port2> ...
```

### 参数说明

| 参数位置      | 参数类型   | 说明                                      |
| ------------- | ---------- | ----------------------------------------- |
| 第 1 个       | `ip_range` | 目标 IP 地址范围（支持 CIDR 格式）或单 IP |
| 第 2 个及以后 | `port`     | 需扫描的目标端口号（可指定多个）          |

## 使用示例

1. **扫描单个 IP 的多个端口**

   ```bash
   python saoip.py 192.168.1.1 80 443 22
   ```

2. **扫描 IP 段的指定端口**

   ```bash
   python saoip.py 192.168.1.0/24 80
   ```

3. **混合扫描模式**
   ```bash
   python saoip.py 192.168.1.0/28 80 443 8080
   ```

## 输出说明

- **成功连接**：
  ```
  192.168.1.1 80 15ms
  ```
- **超时/拒绝**：
  - 自动静默过滤超时和被拒绝的连接
- **错误信息**：
  ```
  Error scanning 192.168.1.1:81: [Errno 10061] Connection refused
  ```

## 注意事项

1. **权限要求**：

   - Windows 系统需要管理员权限运行(不用)
   - Linux/Mac 需确保有足够 socket 权限

2. **网络环境**：

   - 扫描结果可能受防火墙策略影响
   - 大规模 IP 段扫描可能触发安全警报

3. **性能建议**：
   - 默认 100 线程并发，可通过修改`max_workers=100`调整
   - 扫描大量 IP 时建议降低并发数避免网络拥塞

## 依赖库

- 标准库（无需额外安装）：
  ```python
  import ipaddress
  import socket
  import sys
  import time
  from concurrent.futures import ThreadPoolExecutor, as_completed
  ```

## 协议声明

MIT License
