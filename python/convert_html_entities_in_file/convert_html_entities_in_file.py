import sys
import html


def convert_html_entities_in_file(input_file_path, output_file_path):
    # 尝试打开输入文件并读取内容
    try:
        with open(input_file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # 将HTML实体转换为对应的字符
        converted_content = html.unescape(content)

        # 将转换后的内容写入输出文件
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(converted_content)

        # 打印成功信息
        print(f"转换完成。结果已保存到 {output_file_path}")

    # 捕获文件未找到的异常
    except FileNotFoundError:
        print(f"未找到路径为 {input_file_path} 的文件。")
    # 捕获其他可能的异常
    except Exception as e:
        print(f"发生错误: {e}")


def main():
    # 检查命令行参数的数量是否正确
    if len(sys.argv) != 3:
        print("用法: python convert_html_entities.py <输入文件> <输出文件>")
    else:
        # 获取输入文件和输出文件的路径
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        # 调用函数进行HTML实体转换
        convert_html_entities_in_file(input_file_path, output_file_path)


# 程序入口
if __name__ == "__main__":
    main()
