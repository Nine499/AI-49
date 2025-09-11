"""
Cosplay文件处理脚本2

此脚本用于处理cosplay相关的文件，主要功能包括：
1. 删除指定目录下的所有非.webp文件
2. 删除所有空文件夹
3. 将处理后的目录压缩为.7z格式
"""

import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# 定义固定目录路径
# 这是需要处理的根目录
fixed_directory = r"C:\Users\fortynine\acg\1"

# 定义7z.exe的路径
# 7-Zip是一个开源的文件压缩工具，支持多种压缩格式
seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"

# 创建线程锁，用于保护共享资源
print_lock = Lock()


def delete_single_file(file_path):
    """
    删除单个非.webp文件。

    Args:
        file_path (str): 文件的完整路径
    """
    try:
        # 使用更安全的方法删除文件
        try:
            os.remove(file_path)
            with print_lock:
                print(f"已删除 {file_path}")
        except PermissionError:
            # 如果直接删除失败，尝试先清除只读属性
            os.chmod(file_path, 0o777)
            os.remove(file_path)
            with print_lock:
                print(f"已删除 {file_path}")
        except Exception as e:
            with print_lock:
                print(f"删除 {file_path} 时出错: {e}")
        return True
    except OSError as e:
        with print_lock:
            print(f"删除 {file_path} 时出错: {e}")
        return False
    except Exception as e:
        with print_lock:
            print(f"处理 {file_path} 时发生未知错误: {e}")
        return False


def delete_non_webp_files(directory):
    """
    删除指定目录及其子目录下的所有非.webp文件。

    Args:
        directory (str): 需要处理的目标目录路径
    """
    # 检查目标目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 {directory} 不存在")
        return

    # 收集所有需要删除的非.webp文件
    non_webp_files = []
    print("正在扫描非.webp文件...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件是否不是.webp文件
            if not file.endswith(".webp"):
                non_webp_files.append(file_path)

    if not non_webp_files:
        print("未找到需要删除的非.webp文件")
        return

    print(f"找到 {len(non_webp_files)} 个非.webp文件，开始多线程删除...")

    # 使用线程池处理所有非.webp文件
    # 线程数设置为CPU核心数+1，但不超过10个线程
    cpu_count = os.cpu_count() or 1
    max_workers = min(cpu_count + 1, 10)
    successful_count = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_file = {
            executor.submit(delete_single_file, file_path): file_path
            for file_path in non_webp_files
        }

        # 处理完成的任务
        for future in as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                success = future.result()
                if success:
                    successful_count += 1
            except Exception as e:
                with print_lock:
                    print(f"处理 {file_path} 时发生异常: {e}")

    print(f"删除完成，成功处理 {successful_count}/{len(non_webp_files)} 个文件")


def remove_empty_folders(directory):
    """
    删除指定目录及其子目录下的所有空文件夹。

    Args:
        directory (str): 需要处理的目标目录路径
    """
    # 检查目标目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 {directory} 不存在")
        return

    # 自底向上遍历目录中的所有文件夹
    # reverse=True确保从最深层的目录开始处理
    # 这样可以确保删除子目录后可能变为空的父目录也能被正确删除
    print("开始删除空文件夹...")
    for root, dirs, _ in sorted(os.walk(directory), reverse=True):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)

            # 检查文件夹是否为空
            # os.listdir(folder_path)返回目录中的文件和文件夹列表
            # 如果列表为空，则该目录为空目录
            try:
                if not os.listdir(folder_path):
                    # 使用更安全的方法删除空文件夹
                    try:
                        os.rmdir(folder_path)
                        print(f"已删除空文件夹 {folder_path}")
                    except PermissionError:
                        # 如果直接删除失败，尝试先清除只读属性
                        os.chmod(folder_path, 0o777)
                        os.rmdir(folder_path)
                        print(f"已删除空文件夹 {folder_path}")
                    except Exception as e:
                        print(f"删除空文件夹 {folder_path} 时出错: {e}")
            except PermissionError:
                print(f"权限不足，无法检查文件夹 {folder_path}")
            except OSError as e:
                print(f"检查空文件夹 {folder_path} 时出错: {e}")
            except Exception as e:
                print(f"处理空文件夹 {folder_path} 时发生未知错误: {e}")


def compress_single_folder(item_path, output_archive_path):
    """
    压缩单个文件夹为.7z格式。

    Args:
        item_path (str): 要压缩的文件夹路径
        output_archive_path (str): 输出的压缩包路径
    """
    try:
        with print_lock:
            print(f"正在压缩 {item_path} 到 {output_archive_path}...")
        # 使用7z压缩文件夹
        # 参数说明:
        # "a" 表示添加文件到压缩包
        # output_archive_path 是输出的压缩包路径
        # item_path 是要压缩的子目录
        subprocess.run(
            [seven_zip_path, "a", output_archive_path, item_path],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",  # 忽略编码错误
        )
        with print_lock:
            print(f"成功压缩 {item_path} 到 {output_archive_path}")
        return True
    except subprocess.CalledProcessError as e:
        with print_lock:
            print(f"压缩 {item_path} 时出错: {e}")
            if e.stderr:
                print(f"错误详情: {e.stderr}")
        return False
    except Exception as e:
        with print_lock:
            print(f"压缩 {item_path} 时发生未知错误: {e}")
        return False


def compress_subfolders(directory):
    """
    将指定目录下的第一层子目录分别压缩为独立的.7z压缩包。

    Args:
        directory (str): 需要压缩的目标目录路径
    """
    # 检查目标目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 {directory} 不存在")
        return

    # 检查7z程序是否存在
    if not os.path.exists(seven_zip_path):
        print(f"错误: 7-Zip程序未找到，请检查路径 {seven_zip_path}")
        return

    # 收集所有需要压缩的子目录
    subfolders_to_compress = []
    print("正在扫描子文件夹...")
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # 只处理目录，跳过文件
        if os.path.isdir(item_path):
            # 压缩包输出路径（在父目录中）
            # 每个第一层子目录压缩成独立的.7z文件
            output_archive_path = os.path.join(directory, f"{item}.7z")
            subfolders_to_compress.append((item_path, output_archive_path))

    if not subfolders_to_compress:
        print("未找到需要压缩的子文件夹")
        return

    print(f"找到 {len(subfolders_to_compress)} 个子文件夹，开始多线程压缩...")

    # 使用线程池处理所有子目录压缩
    # 线程数设置为CPU核心数+1，但不超过10个线程
    cpu_count = os.cpu_count() or 1
    max_workers = min(cpu_count + 1, 10)
    successful_count = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_folder = {
            executor.submit(compress_single_folder, item_path, output_archive_path): (
                item_path,
                output_archive_path,
            )
            for item_path, output_archive_path in subfolders_to_compress
        }

        # 处理完成的任务
        for future in as_completed(future_to_folder):
            item_path, output_archive_path = future_to_folder[future]
            try:
                success = future.result()
                if success:
                    successful_count += 1
            except Exception as e:
                with print_lock:
                    print(f"处理 {item_path} 时发生异常: {e}")

    print(
        f"压缩完成，成功处理 {successful_count}/{len(subfolders_to_compress)} 个文件夹"
    )


def main():
    """
    主函数：执行文件处理流程
    """
    # 检查目标目录是否存在
    if not os.path.exists(fixed_directory):
        print(f"错误: 目标目录 {fixed_directory} 不存在，请检查路径设置")
        sys.exit(1)

    # 添加确认提示，防止误操作
    print("=== Cosplay文件处理脚本2 ===")
    print(f"目标目录: {fixed_directory}")
    print("本脚本将执行以下操作:")
    print("1. 删除所有非.webp文件")
    print("2. 删除所有空文件夹")
    print("3. 将目录压缩为.7z格式")
    print("\n注意: 此操作不可逆，请确保已备份重要文件!")

    user_input = input(
        "\n你真的要执行吗？\n这是cosplay2。这是cosplay2。这是cosplay2。这是cosplay2。\n请输入 'yes' 确认执行: "
    )

    if user_input.lower() != "yes":
        print("操作已取消。")
        return

    print("\n开始执行操作...")
    # 先删除非webp文件
    delete_non_webp_files(fixed_directory)
    # 再删除空文件夹
    remove_empty_folders(fixed_directory)
    # 最后压缩文件夹
    compress_subfolders(fixed_directory)

    print("\n所有操作已完成!")


# 程序入口点
if __name__ == "__main__":
    main()
