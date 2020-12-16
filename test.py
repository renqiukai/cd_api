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


token = "59beb8f8-137f-4c0f-a1ef-03d1fbe6ab35"
a = auth(token)
response = a.update_status(_id="21844", status=1)
logger.info(response)
