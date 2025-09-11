"""
UUID生成器脚本

这个脚本用于生成一个UUIDv4格式的唯一标识符，
并将它复制到系统剪贴板中，方便用户直接粘贴使用。
"""

import uuid
import pyperclip
import sys


def generate_uuid():
    """
    生成UUIDv4并复制到剪贴板

    UUID (Universally Unique Identifier) 是一个128位的标识符，
    通常用于在分布式系统中唯一标识信息。
    UUIDv4是基于随机数生成的UUID。
    """
    try:
        # 生成一个UUIDv4（基于随机数的UUID）
        uuidv4 = uuid.uuid4()

        # 将生成的UUID复制到系统剪贴板
        # 这样用户就可以直接粘贴使用，无需手动复制
        pyperclip.copy(str(uuidv4))

        # 在控制台打印生成的UUID
        print(f"UUID: {uuidv4}")
        print("UUID已复制到剪贴板")

    except pyperclip.PyperclipException:
        # 如果剪贴板操作失败（例如在某些Linux环境中）
        uuidv4 = uuid.uuid4()
        print(f"UUID: {uuidv4}")
        print("警告: 无法访问剪贴板，请手动复制上面的UUID")
    except Exception as e:
        # 捕获其他可能的异常
        print(f"生成UUID时发生错误: {str(e)}")
        sys.exit(1)


def main():
    """
    主函数
    """
    print("正在生成UUID...")
    generate_uuid()


# 程序入口点
# 当直接运行此脚本时执行main函数
if __name__ == "__main__":
    main()
