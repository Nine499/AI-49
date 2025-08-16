import requests


def main():
    # 发送请求并获取JSON数据
    xinwei_url = "https://60s.viki.moe/v2/60s"
    neirong_xinwei_url = requests.get(xinwei_url)
    json_xinwei_url = neirong_xinwei_url.json()

    # 提取并打印新闻列表
    for i, news_item in enumerate(json_xinwei_url["data"]["news"], 1):
        print(f"{i}. {news_item}")
    input("\n按回车键退出...")


if __name__ == "__main__":
    main()
