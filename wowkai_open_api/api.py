"""
接口用于中间层和wowkai平台打通。
"""

from logging import log
from pymysql import DATETIME
import requests
from requests.models import Response
from loguru import logger
import time
import json


class tokenFail(BaseException):
    ...


class apiRequestFail(BaseException):
    ...


class wowkaiApi:
    host_name = ""
    token = ""

    def __init__(self) -> None:
        pass

    def request_token(self):
        client_id = "41aa2e34-e044-11ea-bf14-8ef63471dacb"
        client_secret = "CQDRNLZGVKQANMABLBOKRGDXOFTCTJUQCDQHCLERLYYZTYKCZN"
        url = "https://oauth.wowkai.cn/oauth2/token"
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json()
            response_data = result.get("data")
            token = response_data.get("access_token")
            expires_in = response_data.get("expires_in")
            token_type = response_data.get("token_type")

            # 请求完后需求增加写入缓存
            self.token = token
            return token
        fail_msg = {
            "status_code": response.status_code,
            "msg": "token请求失败。",
        }
        raise tokenFail(fail_msg)

    def get_token(self):
        return self.request_token()

    def request(
            self, params=None,
            json_data=None, method="POST"
    ):
        # url = f"{self.host_name}{api_name}"
        url = "https://api.wowkai.cn/adapter"
        headers = {
            "Authorization": f"Bearer {self.get_token()}",
        }
        logger.debug(json_data)
        logger.debug(headers)
        response = requests.post(url=url, headers=headers, json=json_data)
        if response.status_code == 200:
            return self.response(response.json())
        fail_msg = {
            "status_code": response.status_code,
            "msg": "请求失败",
            "data": json_data,
        }
        raise apiRequestFail(fail_msg)

    def response(self, data):
        logger.debug(data)
        return data

    def guide_sync(self,
                   emp_code=None,
                   emp_name=None,
                   emp_phone=None,
                   shop_code=None,
                   ):
        data = {
            "method": "cd.shop.guide.sync",
            "time": str(int(time.time()*1000)),
            "emp_type": 1
        }
        if emp_code:
            data["emp_code"] = emp_code
        if emp_name:
            data["emp_name"] = emp_name
        if emp_phone:
            data["emp_phone"] = emp_phone
        if shop_code:
            data["shop_code"] = shop_code
        return self.request(json_data=data)


if __name__ == "__main__":
    w = wowkaiApi()
    data = {
        "emp_code": "13801587423",
        "emp_name": "任秋锴",
        "emp_phone": "13801587423",
        "shop_code": "O1323087",
    }
    w.guide_sync(**data)
    # logger.debug(w.get_token())
