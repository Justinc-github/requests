import requests

url = "https://www.baidu.com/"

response = requests.get(url)

# print(response.content.decode())
# print(len(response.content.decode()))
# 构建请求头字典
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

response1 = requests.get(url, headers=headers)
# print(len(response1.content.decode()))
print(response1.content.decode())
