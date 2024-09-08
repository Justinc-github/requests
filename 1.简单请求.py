# import requests
#
# url = "http://www.baidu.com/"
# response = requests.get(url)
# print(response.text)  # 打印返回内容


# import requests
#
# url = "http://www.baidu.com/"
#
# response = requests.get(url)
#
# # 手动设置编码格式
# response.encoding = "utf8"
#
# # # 打印响应内容
# # print(response.text)
#
# # response.content是存储的bytes类型的响应源码，可以进行decode操作
# print(response.content.decode())

import requests

# 拿到百度首页的url地址，临时存储至变量
url = "http://www.baidu.com/"

# 向百度首页发起请求，并且返回响应，将返回的数据赋值给response
response = requests.get(url)

# 设置响应编码为utf-8，防止出现乱码
response.encoding = "utf-8"

# 此处打印response结果为200，即为请求成功
print(response.content.decode())

# 在静态网页当中，响应数据即为对应url的源代码
