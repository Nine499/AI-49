"""
Cosplay文件处理脚本1

此脚本用于处理cosplay相关的文件，主要功能包括：
1. 解压指定目录下的所有压缩文件（zip, rar, 7z）
2. 删除解压后的原压缩文件
3. 删除指定目录下的所有.webp和.gif文件
"""

import os
import subprocess
import sys

# 定义固定目录路径
# 这是需要处理的根目录
fixed_directory = r"C:\Users\fortynine\acg\1"

# 定义7z.exe的路径
# 7-Zip是一个开源的文件压缩工具，支持多种压缩格式
seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"


def extract_and_delete_archives(directory):
    """
    解压指定目录下的所有压缩文件，并删除原压缩文件。

    Args:
        directory (str): 需要处理的目标目录路径
    """
    # 检查目标目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 {directory} 不存在")
        return

    # 检查7z程序是否存在
    if not os.path.exists(seven_zip_path):
        print(f"错误: 7-Zip程序未找到，请检查路径 {seven_zip_path}")
        return

    # 遍历目录中的所有文件
    # os.walk()会递归遍历目录树
    # root: 当前遍历的目录路径
    # dirs: 当前目录下的子目录列表
    # files: 当前目录下的文件列表
    print("开始解压文件...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 构造完整的文件路径
            file_path = os.path.join(root, file)

            # 检查文件是否为压缩文件（支持zip, rar, 7z等常见格式）
            if file.endswith((".zip", ".rar", ".7z")):
                try:
                    print(f"正在解压 {file_path}...")
                    # 使用7z解压文件
                    # 参数说明:
                    # "x" 表示解压并保持完整路径
                    # "-o" + root 表示解压到当前目录
                    # "-y" 表示对所有询问回答"是"
                    # 使用字符串格式确保路径正确处理
                    subprocess.run(
                        [seven_zip_path, "x", file_path, f"-o{root}", "-y"],
                        check=True,
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        errors="ignore",  # 忽略编码错误
                    )
                    print(f"成功解压 {file_path}")

                    # 删除原压缩文件，使用更安全的方法
                    try:
                        os.remove(file_path)
                        print(f"已删除原压缩文件 {file_path}")
                    except PermissionError:
                        # 如果直接删除失败，尝试先清除只读属性
                        os.chmod(file_path, 0o777)
                        os.remove(file_path)
                        print(f"已删除原压缩文件 {file_path}")
                    except Exception as e:
                        print(f"删除 {file_path} 时出错: {e}")

                except subprocess.CalledProcessError as e:
                    print(f"解压 {file_path} 时出错: {e}")
                    if e.stderr:
                        print(f"错误详情: {e.stderr}")
                except PermissionError:
                    print(f"权限不足，无法处理 {file_path}")
                except OSError as e:
                    print(f"操作系统错误，处理 {file_path} 时出错: {e}")
                except Exception as e:
                    print(f"处理 {file_path} 时发生未知错误: {e}")


def delete_specific_files(directory):
    """
    删除指定目录及其子目录下的所有.webp和.gif文件。

    Args:
        directory (str): 需要处理的目标目录路径
    """
    # 检查目标目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 {directory} 不存在")
        return

    # 遍历目录中的所有文件
    print("开始删除.webp和.gif文件...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # 检查文件是否为.webp或.gif文件
            if file.endswith((".webp", ".gif")):
                try:
                    # 使用更安全的方法删除文件
                    try:
                        os.remove(file_path)
                        print(f"已删除 {file_path}")
                    except PermissionError:
                        # 如果直接删除失败，尝试先清除只读属性
                        os.chmod(file_path, 0o777)
                        os.remove(file_path)
                        print(f"已删除 {file_path}")
                    except Exception as e:
                        print(f"删除 {file_path} 时出错: {e}")
                except OSError as e:
                    print(f"删除 {file_path} 时出错: {e}")
                except Exception as e:
                    print(f"处理 {file_path} 时发生未知错误: {e}")


def main():
    """
    主函数：执行文件处理流程
    """
    # 检查目标目录是否存在
    if not os.path.exists(fixed_directory):
        print(f"错误: 目标目录 {fixed_directory} 不存在，请检查路径设置")
        sys.exit(1)

    # 添加确认提示，防止误操作
    print("=== Cosplay文件处理脚本1 ===")
    print(f"目标目录: {fixed_directory}")
    print("本脚本将执行以下操作:")
    print("1. 解压所有压缩文件(.zip, .rar, .7z)")
    print("2. 删除解压后的原压缩文件")
    print("3. 删除所有.webp和.gif文件")
    print("\n注意: 此操作不可逆，请确保已备份重要文件!")

    user_input = input(
        "\n你真的要执行吗？\n这是cosplay1。这是cosplay1。这是cosplay1。这是cosplay1。\n请输入 'yes' 确认执行: "
    )

    if user_input.lower() != "yes":
        print("操作已取消。")
        return

    print("\n开始执行操作...")
    # 先解压并删除压缩文件
    extract_and_delete_archives(fixed_directory)
    # 再删除特定文件
    delete_specific_files(fixed_directory)

    print("\n所有操作已完成!")


# 程序入口点
if __name__ == "__main__":
    main()
