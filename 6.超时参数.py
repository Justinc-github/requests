import requests

url = "https://cms.youtube.com/"

response = requests.get(url, timeout=3)  # 访问时间超时3秒则抛出异常
