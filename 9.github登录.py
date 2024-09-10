import time

import requests
import re


def login():
    # 获取token
    url1 = "https://github.com/login"
    session = requests.session()
    session.headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }

    res_1 = session.get(url1).content.decode()
    token = re.findall('<input type="hidden" data-csrf="true" name="authenticity_token" value="(.*?)" />'
                       , res_1)[0]
    print(f"获取成功，token为: {token}")
    # 登录
    url2 = "https://github.com/session"
    data = {
        "commit": "Sign in",
        "authenticity_token": token,
        "add_account": "",
        "login": "1927705375@qq.com",
        "password": "SJCsjc0315!",
        "webauthn-conditional": "undefined",
        "javascript-support": "true",
        "webauthn-support": "supported",
        "webauthn-iuvpaa-support": "unsupported",
        "return_to": "https://github.com/login",
        # "allow_signup": "",
        # "client_id": "",
        # "integration": "",
        # "required_field_5e5f": "",
        "timestamp": time.time() * 1000,
        "timestamp_secret": "ed50ee1652fb00e6084a47feb0e630588947f2faa4b9f0f978248c5d7ce8b3f7"
    }
    session.post(url2, data=data)
    print("登录成功")
    # 验证
    url3 = "https://github.com/Justinc-github"
    response = session.get(url3)
    with open("github.html", "wb") as f:
        f.write(response.content)
    print("验证通过")


if __name__ == '__main__':
    login()
