import sys
import cloudscraper
import re


def sanitize_filename(filename):
    """清洗非法字符的函数"""
    # 替换所有非法字符为下划线
    cleaned = re.sub(r'[\\/:*?"<>|]', "_", filename)
    # 去除首尾空格并限制长度
    cleaned = cleaned.strip()[:50]
    return cleaned or "default"  # 如果为空则返回默认名称


def download_file():
    if len(sys.argv) > 1:
        book_id = sys.argv[1]
    else:
        book_id = input("请输入书籍ID数字: ")
    url = f"https://dl.wenku8.com/down.php?type=utf8&node=1&id={book_id}"

    try:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url)
        response.raise_for_status()

        lines = response.text.splitlines()

        if len(lines) >= 3:
            # 清洗文件名并添加扩展名
            raw_name = lines[2].strip()
            clean_name = sanitize_filename(raw_name)
            filename = f"{clean_name}.txt"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"文件已保存为：{filename}")
        else:
            print("文件内容不足三行，无法获取文件名")

    except Exception as e:
        print(f"操作失败: {str(e)}")


if __name__ == "__main__":
    download_file()
