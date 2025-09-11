#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
版本更新脚本

此脚本用于自动更新项目中的版本号，并安装最新的whl文件。
功能包括：
1. 查找并删除项目中的dist文件夹
2. 查找项目中的pyproject.toml文件，并将版本号更新为当前时间戳格式
3. 在工作目录执行uv build
4. 在工作目录及其子目录中查找最新的whl文件
5. 使用uv工具安装最新的whl文件
"""

import os
import sys
import shutil
from datetime import datetime
from typing import Union
import toml
import subprocess


def find_and_remove_dist_folder(start_path: str, max_depth: int = 3) -> bool:
    """
    在指定目录及其子目录中查找并删除dist文件夹

    Args:
        start_path (str): 开始搜索的目录路径
        max_depth (int): 最大搜索深度，默认为3层

    Returns:
        bool: 删除成功返回True，否则返回False
    """
    print(f"正在目录 {start_path} 中查找 dist 文件夹...")

    # 使用os.walk遍历目录树
    for root, dirs, files in os.walk(start_path):
        # 计算当前目录的深度
        depth = root[len(start_path) :].count(os.sep)

        # 检查当前目录是否包含dist文件夹
        if "dist" in dirs:
            dist_path = os.path.join(root, "dist")
            try:
                # 删除整个dist文件夹
                shutil.rmtree(dist_path)
                print(f"成功删除 dist 文件夹: {dist_path}")
                return True
            except Exception as e:
                print(f"删除 dist 文件夹时出错: {e}")
                return False

        # 如果达到最大搜索深度，则停止继续深入搜索
        if depth >= max_depth - 1:
            # 清空dirs列表，防止os.walk继续递归遍历子目录
            dirs.clear()

    print("未找到 dist 文件夹")
    return True


def find_pyproject_toml(start_path: str, max_depth: int = 3) -> Union[str, None]:
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
            dirs.clear()

    # 如果未找到pyproject.toml文件，返回None
    return None


def update_version_in_pyproject(file_path: str) -> bool:
    """
    更新pyproject.toml文件中的版本号

    Args:
        file_path (str): pyproject.toml文件的路径

    Returns:
        bool: 更新成功返回True，否则返回False
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


def run_uv_build(work_dir: str) -> bool:
    """
    在指定工作目录执行uv build命令

    Args:
        work_dir (str): 工作目录路径

    Returns:
        bool: 构建成功返回True，否则返回False
    """
    try:
        print(f"正在工作目录 {work_dir} 中执行 uv build...")

        # 直接执行uv build命令
        cmd = ["uv", "build"]

        # 执行命令
        result = subprocess.run(
            cmd, cwd=work_dir, capture_output=True, text=True, check=True
        )

        print("uv build 执行成功!")
        if result.stdout:
            print(f"构建输出: {result.stdout}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"执行uv build时出错: {e}")
        if e.stderr:
            print(f"错误输出: {e.stderr}")
        return False
    except FileNotFoundError:
        print("错误: 找不到uv工具，请确保已安装uv")
        return False
    except Exception as e:
        print(f"执行uv build时发生未知错误: {e}")
        return False


def find_latest_wheel(start_path: str, max_depth: int = 2) -> Union[str, None]:
    """
    在指定目录及其子目录中查找最新的whl文件

    Args:
        start_path (str): 开始搜索的目录路径
        max_depth (int): 最大搜索深度，默认为2层

    Returns:
        str or None: 找到的最新whl文件路径，如果未找到则返回None
    """
    print(f"正在目录 {start_path} 中查找最新的whl文件，最大深度: {max_depth} 层...")

    wheel_files = []

    # 使用os.walk遍历目录树
    for root, dirs, files in os.walk(start_path):
        # 计算当前目录的深度
        depth = root[len(start_path) :].count(os.sep)

        # 查找所有whl文件
        for file in files:
            if file.endswith(".whl"):
                wheel_path = os.path.join(root, file)
                wheel_files.append((wheel_path, os.path.getmtime(wheel_path)))
                print(f"找到whl文件: {wheel_path}")

        # 如果达到最大搜索深度，则停止继续深入搜索
        if depth >= max_depth - 1:
            # 清空dirs列表，防止os.walk继续递归遍历子目录
            dirs.clear()

    if not wheel_files:
        print("未找到任何whl文件")
        return None

    # 根据文件修改时间找到最新的whl文件
    latest_wheel_path, _ = max(wheel_files, key=lambda x: x[1])
    print(f"最新的whl文件: {latest_wheel_path}")
    return latest_wheel_path


def install_wheel_with_uv(wheel_path: str) -> bool:
    """
    使用uv工具安装指定的whl文件

    Args:
        wheel_path (str): whl文件的路径

    Returns:
        bool: 安装成功返回True，否则返回False
    """
    try:
        print(f"正在使用uv工具安装whl文件: {wheel_path}")

        # 构造uv工具安装命令
        cmd = ["uv", "tool", "install", wheel_path]

        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        print("whl文件安装成功!")
        if result.stdout:
            print(f"安装输出: {result.stdout}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"安装whl文件时出错: {e}")
        if e.stderr:
            print(f"错误输出: {e.stderr}")
        return False
    except FileNotFoundError:
        print("错误: 找不到uv工具，请确保已安装uv")
        return False
    except Exception as e:
        print(f"安装whl文件时发生未知错误: {e}")
        return False


def main():
    """
    主函数：按顺序执行以下操作：
    1. 查找并删除dist文件夹
    2. 查找pyproject.toml文件并更新版本号
    3. 在工作目录执行uv build
    4. 查找最新的whl文件
    5. 使用uv工具安装最新的whl文件
    """
    print("=== 版本更新工具 ===")

    # 获取当前工作目录作为搜索起点
    start_directory = os.getcwd()
    print(f"当前工作目录: {start_directory}")

    # 第一步：查找并删除dist文件夹
    print("\n=== 删除dist文件夹 ===")
    remove_success = find_and_remove_dist_folder(start_directory)
    if not remove_success:
        print("删除dist文件夹失败！")
        sys.exit(1)

    # 第二步：查找pyproject.toml文件并更新版本号
    print("\n=== 更新版本号 ===")
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

    # 第三步：在工作目录执行uv build
    print("\n=== 执行uv build ===")
    build_success = run_uv_build(start_directory)
    if not build_success:
        print("uv build执行失败！")
        sys.exit(1)

    # 第四步和第五步：查找最新的whl文件并安装
    print("\n=== whl文件安装 ===")
    latest_wheel = find_latest_wheel(start_directory)

    if latest_wheel:
        install_success = install_wheel_with_uv(latest_wheel)
        if not install_success:
            print("whl文件安装失败！")
            sys.exit(1)
    else:
        print("未找到whl文件，跳过安装步骤")


# 程序入口点
if __name__ == "__main__":
    main()
