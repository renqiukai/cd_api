'''
@说明    :草动开放平台基础方法
@时间    :2020/2/13 下午4:28:26
@作者    :任秋锴
@版本    :1.0
'''
import requests
from loguru import logger


class base:
    def __init__(self, token):
        self.token = token

    def request(self, method="GET", **kwargs):
        api_address = f"https://api.wowkai.cn/adapter"
        headers = {
            "Authorization": f"Bearer {self.token}",
        }
        kwargs["headers"] = headers
        response = requests.request(method=method, url=api_address, **kwargs)
        if response.status_code == 200:
            return self.response(response.json())

    def response(self, response_json):
        status = response_json.get("status")
        if status == 200:
            return response_json.get("data")
        else:
            print(response_json)
