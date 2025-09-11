"""
SAO IP工具 - 用于扫描和测试IP地址连通性

功能：
1. 使用ICMP协议测试IP地址连通性 (ping)
2. 使用TCP协议测试指定端口的连通性
3. 支持CIDR格式的IP地址段扫描
4. 输出连通的IP地址及响应时间

使用方法：
- ICMP测试: saoip.py 192.168.1.1 或 saoip.py 192.168.1.1/24
- TCP测试: saoip.py 192.168.1.1 80 或 saoip.py 192.168.1.1/24 80,443,81-8080
"""

import sys
import socket
import ipaddress
import subprocess
import time
import platform
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


# 线程锁用于安全输出
print_lock = threading.Lock()


def parse_ports(port_str):
    """
    解析端口字符串，支持逗号分隔和范围表示

    Args:
        port_str (str): 端口字符串，如 "80,443,81-8080"

    Returns:
        list: 端口列表
    """
    ports = []
    # 按逗号分割
    for part in port_str.split(","):
        if "-" in part:
            # 处理范围，如 81-8080
            start, end = part.split("-")
            ports.extend(range(int(start), int(end) + 1))
        else:
            # 单个端口
            ports.append(int(part))
    return ports


def ping_ip(ip, timeout=1):
    """
    使用ICMP协议ping指定IP地址

    Args:
        ip (str): IP地址
        timeout (int): 超时时间（秒）

    Returns:
        tuple: (是否连通, 响应时间ms)
    """
    try:
        # 根据操作系统选择ping命令
        if platform.system().lower() == "windows":
            # Windows系统
            cmd = ["ping", "-n", "1", "-w", str(timeout * 1000), str(ip)]
        else:
            # Linux/Mac系统
            cmd = ["ping", "-c", "1", "-W", str(timeout), str(ip)]

        start_time = time.time()
        # 执行ping命令
        result = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        end_time = time.time()

        # 计算响应时间（毫秒）
        response_time = (end_time - start_time) * 1000

        # 判断是否ping通
        if result.returncode == 0:
            return True, response_time
        else:
            return False, None
    except Exception:
        return False, None


def tcp_connect(ip, port, timeout=1):
    """
    使用TCP连接测试指定IP的端口

    Args:
        ip (str): IP地址
        port (int): 端口号
        timeout (int): 超时时间（秒）

    Returns:
        tuple: (是否连通, 响应时间ms)
    """
    try:
        # 创建TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        start_time = time.time()
        # 尝试连接
        result = sock.connect_ex((str(ip), port))
        end_time = time.time()

        # 计算响应时间（毫秒）
        response_time = (end_time - start_time) * 1000

        # 关闭socket
        sock.close()

        # 判断是否连接成功
        if result == 0:
            return True, response_time
        else:
            return False, None
    except Exception:
        return False, None


def parse_ip_range(ip_str):
    """
    解析IP地址或CIDR格式的IP段

    Args:
        ip_str (str): IP地址或CIDR格式的IP段

    Returns:
        list: IP地址列表
    """
    try:
        # 尝试解析为CIDR格式的网络
        network = ipaddress.ip_network(ip_str, strict=False)
        return list(network.hosts())
    except ValueError:
        try:
            # 尝试解析为单个IP地址
            ip = ipaddress.ip_address(ip_str)
            return [ip]
        except ValueError:
            # 无效的IP地址格式
            print(f"错误: 无效的IP地址格式 '{ip_str}'")
            return []


def scan_icmp_worker(ip):
    """
    ICMP扫描工作线程函数

    Args:
        ip (IPAddress): IP地址对象
    """
    is_alive, response_time = ping_ip(ip)
    if is_alive:
        with print_lock:
            print(f"IP: {ip} 通 ({response_time:.2f} ms)")


def scan_tcp_worker(ip, port):
    """
    TCP扫描工作线程函数

    Args:
        ip (IPAddress): IP地址对象
        port (int): 端口号
    """
    is_open, response_time = tcp_connect(ip, port)
    if is_open:
        with print_lock:
            print(f"IP: {ip} 端口: {port} 开放 ({response_time:.2f} ms)")


def scan_icmp(ips):
    """
    使用ICMP协议扫描IP地址列表（多线程并行处理）

    Args:
        ips (list): IP地址列表
    """
    print("使用ICMP协议测试IP连通性...")
    print("-" * 50)

    # 使用线程池并发执行ping操作
    with ThreadPoolExecutor(max_workers=100) as executor:
        # 提交所有任务
        future_to_ip = {executor.submit(scan_icmp_worker, ip): ip for ip in ips}

        # 等待所有任务完成
        for future in as_completed(future_to_ip):
            try:
                future.result()
            except Exception:
                pass


def scan_tcp(ips, ports):
    """
    使用TCP协议扫描IP地址和端口组合（多线程并行处理）

    Args:
        ips (list): IP地址列表
        ports (list): 端口列表
    """
    print("使用TCP协议测试端口连通性...")
    print("-" * 50)

    # 使用线程池并发执行TCP连接测试
    with ThreadPoolExecutor(max_workers=100) as executor:
        # 提交所有任务
        future_to_ip_port = {
            executor.submit(scan_tcp_worker, ip, port): (ip, port)
            for ip in ips
            for port in ports
        }

        # 等待所有任务完成
        for future in as_completed(future_to_ip_port):
            try:
                future.result()
            except Exception:
                pass


def main():
    """
    主函数 - 处理命令行参数并执行相应操作
    """
    # 检查命令行参数数量
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  ICMP测试: saoip.py <IP地址或IP段>")
        print("  TCP测试: saoip.py <IP地址或IP段> <端口列表>")
        print()
        print("示例:")
        print("  saoip.py 192.168.1.1")
        print("  saoip.py 192.168.1.1/24")
        print("  saoip.py 192.168.1.1 80")
        print("  saoip.py 192.168.1.1/24 80,443")
        print("  saoip.py 192.168.1.1/24 80,443,81-8080")
        return

    # 解析IP地址或IP段
    ip_str = sys.argv[1]
    ips = parse_ip_range(ip_str)

    if not ips:
        print(f"错误: 无法解析IP地址或IP段 '{ip_str}'")
        return

    # 判断是ICMP测试还是TCP测试
    if len(sys.argv) == 2:
        # ICMP测试
        scan_icmp(ips)
    elif len(sys.argv) == 3:
        # TCP测试
        port_str = sys.argv[2]
        try:
            ports = parse_ports(port_str)
            if not ports:
                print(f"错误: 无法解析端口列表 '{port_str}'")
                return
            scan_tcp(ips, ports)
        except ValueError:
            print(f"错误: 端口格式不正确 '{port_str}'")
            return
    else:
        print("错误: 参数数量不正确")
        print("使用方法:")
        print("  ICMP测试: saoip.py <IP地址或IP段>")
        print("  TCP测试: saoip.py <IP地址或IP段> <端口列表>")


# 程序入口点
if __name__ == "__main__":
    main()
