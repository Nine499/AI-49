import os
import subprocess

# 定义固定目录路径
fixed_directory = r"C:\Users\fortynine\acg\1"
# 定义7z.exe的路径
seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"


def delete_non_webp_files(directory):
    """
    删除指定目录及其子目录下的所有非.webp文件。
    :param directory: 目标目录路径
    """
    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件是否不是.webp文件
            if not file.endswith(".webp"):
                try:
                    os.remove(file_path)
                    print(f"已删除 {file_path}")
                except OSError as e:
                    print(f"删除 {file_path} 时出错: {e}")


def remove_empty_folders(directory):
    """
    删除指定目录及其子目录下的所有空文件夹。
    :param directory: 目标目录路径
    """
    # 自底向上遍历目录中的所有文件夹
    for root, dirs, _ in sorted(os.walk(directory), reverse=True):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            # 检查文件夹是否为空
            if not os.listdir(folder_path):
                try:
                    os.rmdir(folder_path)
                    print(f"已删除空文件夹 {folder_path}")
                except OSError as e:
                    print(f"删除空文件夹 {folder_path} 时出错: {e}")


def compress_subfolders(directory):
    """
    将指定目录下的每个子文件夹压缩为独立的.7z压缩包。
    :param directory: 目标目录路径
    """
    # 遍历目录中的所有子文件夹
    for root, dirs, _ in os.walk(directory):
        for dir_name in dirs:
            subfolder_path = os.path.join(root, dir_name)
            output_archive_path = os.path.join(root, f"{dir_name}.7z")
            try:
                # 使用7z压缩文件夹
                subprocess.run(
                    [seven_zip_path, "a", output_archive_path, subfolder_path],
                    check=True,
                )
                print(f"成功压缩 {subfolder_path} 到 {output_archive_path}")
            except subprocess.CalledProcessError as e:
                print(f"压缩 {subfolder_path} 时出错: {e}")


def main():
    delete_non_webp_files(fixed_directory)
    remove_empty_folders(fixed_directory)
    compress_subfolders(fixed_directory)


if __name__ == "__main__":
    main()
