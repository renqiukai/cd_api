'''
@Author: Rqk
@Date: 2020-04-26 15:01:20
@Description: 
'''
from cdApi.coupon_pack import couponPack
from cdApi.product import product
from cdApi.user import user
from cdApi.store import store
from cdApi.auth import auth
import pandas as pd
from loguru import logger
token = "81aa6193-4aaf-4d6b-bdd3-9425faa1fd87"
s = store(token)
result = s.code2id()
print(result.get("007070"))
# a = auth(token)
# for role_info in a.role_list():
#     print(role_info)
