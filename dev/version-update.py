"""
版本更新脚本

此脚本用于自动更新项目中的版本号。
它会查找项目中的pyproject.toml文件，并将版本号更新为当前时间戳格式。
"""

import os
import sys
from datetime import datetime
import toml


def find_pyproject_toml(start_path, max_depth=3):
    """
    在指定目录及其子目录中查找pyproject.toml文件

    Args:
        start_path (str): 开始搜索的目录路径
        max_depth (int): 最大搜索深度，默认为3层

    Returns:
        str or None: 找到的pyproject.toml文件路径，如果未找到则返回None
    """
    print(f"正在目录 {start_path} 中查找 pyproject.toml 文件...")

    # 使用os.walk遍历目录树
    for root, dirs, files in os.walk(start_path):
        # 计算当前目录的深度
        depth = root[len(start_path) :].count(os.sep)

        # 检查当前目录是否包含pyproject.toml文件
        if "pyproject.toml" in files:
            pyproject_path = os.path.join(root, "pyproject.toml")
            print(f"在目录深度 {depth} 处找到 pyproject.toml: {pyproject_path}")
            return pyproject_path

        # 如果达到最大搜索深度，则停止继续深入搜索
        if depth >= max_depth - 1:
            # 清空dirs列表，防止os.walk继续递归遍历子目录
            del dirs[:]

    # 如果未找到pyproject.toml文件，返回None
    return None


def update_version_in_pyproject(file_path):
    """
    更新pyproject.toml文件中的版本号

    Args:
        file_path (str): pyproject.toml文件的路径
    """
    try:
        # 读取pyproject.toml文件内容
        with open(file_path, "r", encoding="utf-8") as file:
            pyproject_data = toml.load(file)

        # 生成当前时间戳作为新版本号
        # 格式为: YYYY.MM.DD.HHMMSS (年.月.日.时分秒)
        current_timestamp = datetime.now().strftime("%Y.%m.%d.%H%M%S")
        print(f"生成新版本号: {current_timestamp}")

        # 检查必要的键是否存在
        if "project" not in pyproject_data:
            print(f"错误: 在 {file_path} 中找不到 'project' 键。请手动添加。")
            return False

        if "version" not in pyproject_data["project"]:
            print(
                f"错误: 在 {file_path} 的 'project' 下找不到 'version' 键。请手动添加。"
            )
            return False

        # 保存旧版本号用于显示
        old_version = pyproject_data["project"]["version"]

        # 更新版本号
        pyproject_data["project"]["version"] = current_timestamp
        print(f"版本号已从 {old_version} 更新为 {current_timestamp}")

        # 将更新后的内容写回文件
        with open(file_path, "w", encoding="utf-8") as file:
            toml.dump(pyproject_data, file)

        print(f"成功更新 {file_path} 文件中的版本号")
        return True

    except FileNotFoundError:
        print(f"错误: 找不到文件 {file_path}")
        return False
    except toml.TomlDecodeError as e:
        print(f"错误: 无法解析TOML文件 {file_path}: {e}")
        return False
    except PermissionError:
        print(f"错误: 没有权限写入文件 {file_path}")
        return False
    except Exception as e:
        print(f"更新版本号时发生未知错误: {e}")
        return False


def main():
    """
    主函数：执行版本更新流程
    """
    print("=== 版本更新工具 ===")

    # 获取当前工作目录作为搜索起点
    start_directory = os.getcwd()
    print(f"当前工作目录: {start_directory}")

    # 查找pyproject.toml文件
    pyproject_path = find_pyproject_toml(start_directory)

    if pyproject_path:
        print(f"找到 pyproject.toml 文件: {pyproject_path}")
        # 更新版本号
        success = update_version_in_pyproject(pyproject_path)
        if success:
            current_version = datetime.now().strftime("%Y.%m.%d.%H%M%S")
            print(f"版本更新成功完成！当前版本: {current_version}")
        else:
            print("版本更新失败！")
            sys.exit(1)
    else:
        print("在指定目录深度内未找到 pyproject.toml 文件。")
        sys.exit(1)


# 程序入口点
if __name__ == "__main__":
    main()
