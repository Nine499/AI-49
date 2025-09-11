"""
每日60秒读懂世界新闻脚本

这个脚本从60s.viki.moe接口获取每日新闻，
并以列表形式在控制台打印出来。
"""

import requests
import sys


def main():
    """
    主函数：获取并显示每日60秒新闻
    """
    # 设置API接口URL
    # 这是一个提供每日60秒新闻的公开API
    xinwei_url = "https://60s.viki.moe/v2/60s"

    try:
        # 发送HTTP GET请求获取JSON数据
        print("正在获取最新新闻...")
        neirong_xinwei_url = requests.get(xinwei_url, timeout=10)

        # 检查HTTP响应状态码
        # 如果状态码不是200会抛出异常
        neirong_xinwei_url.raise_for_status()

        # 解析JSON数据
        json_xinwei_url = neirong_xinwei_url.json()

        # 检查API返回是否成功
        if json_xinwei_url.get("code") != 200:
            print("API返回错误:", json_xinwei_url.get("message", "未知错误"))
            sys.exit(1)

        # 提取并打印新闻列表
        # 从JSON数据中提取新闻列表
        news_list = json_xinwei_url["data"]["news"]

        print("=== 每日60秒读懂世界 ===")
        for i, news_item in enumerate(news_list, 1):
            # 使用enumerate函数从1开始编号
            print(f"{i}. {news_item}")

        print("\n数据获取时间:", json_xinwei_url["data"].get("date", "未知"))
        input("\n按回车键退出...")

    except requests.exceptions.Timeout:
        # 处理请求超时异常
        print("错误: 请求超时，请检查网络连接")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        # 处理网络连接异常
        print("错误: 网络连接失败，请检查网络设置")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        # 处理HTTP错误
        print(f"HTTP错误: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        # 处理其他requests相关异常
        print(f"请求发生错误: {e}")
        sys.exit(1)
    except KeyError as e:
        # 处理JSON数据结构异常
        print(f"数据格式错误，缺少必要字段: {e}")
        sys.exit(1)
    except ValueError as e:
        # 处理JSON解析异常
        print(f"JSON数据解析错误: {e}")
        sys.exit(1)
    except Exception as e:
        # 处理其他未预期的异常
        print(f"发生未知错误: {e}")
        sys.exit(1)


# 程序入口点
if __name__ == "__main__":
    main()
