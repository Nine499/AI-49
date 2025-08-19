import sys
import html


def convert_html_entities_in_file(input_file_path, output_file_path):
    """
    将HTML文件中的HTML实体转换为对应的字符

    HTML实体是一些特殊字符的编码表示，例如:
    &amp;  ->  &
    &lt;   ->  <
    &gt;   ->  >
    &quot; ->  "

    Args:
        input_file_path (str): 输入文件的路径
        output_file_path (str): 输出文件的路径
    """
    # 尝试打开输入文件并读取内容
    try:
        # 使用utf-8编码打开文件，确保能正确处理中文等特殊字符
        with open(input_file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # 将HTML实体转换为对应的字符
        # html.unescape()函数可以将HTML实体转换为对应的字符
        converted_content = html.unescape(content)

        # 将转换后的内容写入输出文件
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(converted_content)

        # 打印成功信息
        print(f"转换完成。结果已保存到 {output_file_path}")

    # 捕获文件未找到的异常
    except FileNotFoundError:
        print(f"错误: 未找到路径为 {input_file_path} 的文件。")
    # 捕获权限错误异常
    except PermissionError:
        print(f"错误: 没有权限访问文件 {input_file_path} 或 {output_file_path}。")
    # 捕获编码错误异常
    except UnicodeDecodeError:
        print(f"错误: 文件 {input_file_path} 编码格式不正确，无法读取。")
    # 捕获其他可能的异常
    except Exception as e:
        print(f"发生未知错误: {e}")


def main():
    """
    主函数，处理命令行参数并调用转换函数
    """
    # 检查命令行参数的数量是否正确
    # 正确的命令格式应该是: python convert_html_entities.py <输入文件> <输出文件>
    # sys.argv[0] 是脚本名称，sys.argv[1] 是输入文件路径，sys.argv[2] 是输出文件路径
    if len(sys.argv) != 3:
        print("用法: python convert_html_entities.py <输入文件> <输出文件>")
        print("示例: python convert_html_entities.py input.html output.html")
        # 程序退出码为1表示执行失败
        sys.exit(1)
    else:
        # 获取输入文件和输出文件的路径
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        # 调用函数进行HTML实体转换
        convert_html_entities_in_file(input_file_path, output_file_path)


# 程序入口
# 当直接运行此脚本时，__name__ 的值为 "__main__"
# 这样可以确保只有直接运行脚本时才会执行main()函数，而作为模块导入时不会执行
if __name__ == "__main__":
    main()
