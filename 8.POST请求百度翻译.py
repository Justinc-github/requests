import json

import requests


class Trans(object):
    def __init__(self, word):
        self.url = "https://fanyi.baidu.com/sug"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        }
        self.data = {
            "kw": word,
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content

    def parse_data(self, data):
        dict_data = json.loads(data)  # 使用loads方法将json字符串转化为python字典
        print(dict_data["data"][0]["v"])

    def run(self):
        response = self.get_data()
        self.parse_data(response)


if __name__ == '__main__':
    word = input("请输入所要翻译的单词:")
    Translate = Trans(word)
    Translate.run()
