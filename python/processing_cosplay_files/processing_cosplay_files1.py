import os
import subprocess

# 定义固定目录路径
fixed_directory = r"C:\Users\fortynine\acg\1"
# 定义7z.exe的路径
seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"


def extract_and_delete_archives(directory):
    """
    解压指定目录下的所有压缩文件，并删除原压缩文件。
    :param directory: 目标目录路径
    """
    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件是否为压缩文件（假设支持zip, rar, 7z等常见格式）
            if file.endswith((".zip", ".rar", ".7z")):
                try:
                    # 使用7z解压文件
                    subprocess.run(
                        [seven_zip_path, "x", file_path, "-o" + root, "-y"], check=True
                    )
                    print(f"成功解压 {file_path}")
                    # 删除原压缩文件
                    os.remove(file_path)
                    print(f"已删除 {file_path}")
                except subprocess.CalledProcessError as e:
                    print(f"解压 {file_path} 时出错: {e}")


def delete_specific_files(directory):
    """
    删除指定目录及其子目录下的所有.webp和.gif文件。
    :param directory: 目标目录路径
    """
    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件是否为.webp或.gif文件
            if file.endswith((".webp", ".gif")):
                try:
                    os.remove(file_path)
                    print(f"已删除 {file_path}")
                except OSError as e:
                    print(f"删除 {file_path} 时出错: {e}")


def main():
    extract_and_delete_archives(fixed_directory)
    delete_specific_files(fixed_directory)


if __name__ == "__main__":
    main()
