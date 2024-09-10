import requests

url = "http://www.baidu.com/"
proxies = {
    # "http": "http://241.252.105.120:64891",
    "https": "http://241.252.105.120:64891"
}
response = requests.get(url, proxies=proxies)
print(response.text)
