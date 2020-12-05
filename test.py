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


token = "b681a8b6-e04c-4cae-b5a1-48cd7bfa14d8"
a = auth(token)
s = store(token)
orgs = s.code2id()
store_info = orgs.get("X1316481")
company_id = store_info.get("company_id")
store_id = store_info.get("store_id")
# for role_info in a.list().get("data").get("dataList"):
#     print(role_info)

params = dict(
    name="任秋锴",
    mobile="13801587423",
    role_ids=[a.get_role_map().get("店长")],
    company_id=company_id,
    store_id=store_id,
    _id=21944,
)

response = a.update_store(**params)
logger.debug(response)
