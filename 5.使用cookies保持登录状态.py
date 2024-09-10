import requests

url = "https://github.com/Justinc-github"

# 构建请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}

# 构建cookies字典
temp = "_octo=GH1.1.1998522517.1720237897; _device_id=d9210b9ff71f5ee4935b0e6e546d1cd2; preferred_color_mode=light; tz=Asia%2FShanghai; saved_user_sessions=131849284%3AHGdgXFAY6_XeGqabbdKxVynYHMlcX_bPs_blO19xWes06BWl; user_session=HGdgXFAY6_XeGqabbdKxVynYHMlcX_bPs_blO19xWes06BWl; __Host-user_session_same_site=HGdgXFAY6_XeGqabbdKxVynYHMlcX_bPs_blO19xWes06BWl; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=Justinc-github; _gh_sess=2XhTGB9CSsYX4wNP2mIHHwmEXaz8t4jDafZtlThiai1zISSbovXTLLe9iUUOlEsFq7GXbE1uq8odzysNAY1DnxtliFYoCfhv8uvk9tUvN6e5lOwKHveZaT9mo%2F9micpeFG0LAAOyJmOKABXlm3eXOlhfFwIdH%2FFPmdSBYPyhSl9uhVF0S%2FKCndVTI7wkVkkXmlfkGz3h%2BErrXv2ZahvcqzD3%2BHHVZsr0MEVB3poXV8anw75ifXUaKu4c3bqsFhYf1%2BEhbwzGwsKGt7bBMopvDn%2FfKWKD9z3ydLVBoOkaFK9fomN67sMk1HazRy5n2s46vOeMF33WH97N0DAZaOXOFlyq%2Fc9HctPkcs5UwUVsgAhnY3rBE8cJkkuiJqOIh2f1ZZB%2By8qr0Ea%2FwJpzjVHI1Swg43LJT5zpJQ%2BUitQJtl%2Fz1A0bHmx7I0SH6m3dHjfY74poY%2BysL3u87k8x%2FYwM8nk897hROELAK8iI6zNvs%2F35w1z7tvIzl%2BRjdIALOilTYDHw7srccoJglmqM4Vs9N%2B5p1PNLeRutbq17fBrSmwx8uTn05WOZdev0LQ8%2B5HgEt44LkmHmsXdXoaB6Y9CVdkgLt77ybUjMV1D%2BuJM069ioJhcNpgnEv2MfceBcrwP5mduZsomFncZjQJYj7g4Zhx%2FU5mmOOdcnVOOh%2FMMjCgOd542g00iWGQnN2QaRt9b7%2B2UR%2Bjl4Orx%2B5iKnNu1P%2F2Bz23Q6SWCw0eTn6b5OZh18aUCF02b2DVBJp2BlwucvhYw3gzn3BC40odUjmrMODdhcnUNyK9t%2B7rW%2BBV0iyLam0t8LRn2QIHyB%2Bfu0mIjnKmtKCNfZtpyP5izEP2KzmvojtUzNHzcWbiISNVViKJ2rCPB0ZcX0AQ%3D%3D--UKTmYCU19bO01YzV--3j50Rs4hv%2Fv7vsIyLVNBWg%3D%3D"
cookie_list = temp.split("; ")
# # 方案一: 循环分割
# cookies = {}
# for cookie in cookie_list:
#     cookies[cookie.split("=")[0]] = cookie.split("=")[-1]

# 方案二: 字典推导式
cookies = {cookie.split("=")[0]: cookie.split("=")[-1] for cookie in cookie_list}

print(cookies)

# 发起一个请求
response = requests.get(url, headers=headers, cookies=cookies)

# 验证是否登录成功
with open("github_cookies.html", "wb") as f:
    f.write(response.content)
print(response.content)

# 依然为登录状态
