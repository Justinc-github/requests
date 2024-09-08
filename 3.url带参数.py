import requests

# url = "https://www.baidu.com/s?wd=python"
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
# }
#
# response = requests.get(url, headers=headers)
#
# with open("baidu.html", "wb") as f:
#     f.write(response.content)


url = "https://www.baidu.com/s?"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# 构建参数字典
data = {
    "wd": "python"
}
response = requests.get(url, headers=headers, params=data)

print(response.url)
