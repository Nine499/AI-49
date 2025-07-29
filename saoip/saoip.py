import ipaddress
import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_ip_port(ip, port):
    try:
        start_time = time.time()
        with socket.create_connection((ip, port), timeout=1):
            delay = int((time.time() - start_time) * 1000)
            return f"{ip} {port} {delay}ms"
    except (socket.timeout, ConnectionRefusedError):
        return None
    except Exception as e:
        return f"Error scanning {ip}:{port}: {str(e)}"


def parse_target(ip_range):
    try:
        network = ipaddress.ip_network(ip_range, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        return [ip_range]


def main():
    if len(sys.argv) < 3:
        print("Usage: python saoip.py <ip_range> <port1> <port2>...")
        return

    ip_range = sys.argv[1]
    ports = list(map(int, sys.argv[2:]))
    ip_list = parse_target(ip_range)

    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_ip = {
            executor.submit(scan_ip_port, ip, port): (ip, port)
            for ip in ip_list
            for port in ports
        }

        for future in as_completed(future_to_ip):
            result = future.result()
            if result and not result.startswith("Error"):
                print(result)


if __name__ == "__main__":
    main()
