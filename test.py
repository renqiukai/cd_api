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
from cdApi.token_api import Token
import pandas as pd
from loguru import logger
from wowkai_open_api.order import order
from wowkai_open_api.coupon import coupon
from wowkai_open_api.logistics import logistics
from wowkai_open_api.token_api import Token
from cdApi.coupon import coupon


token = "cb1abcd9-4670-40c2-995c-db41f271b404"
a = coupon(token)
response = a.read(_id="13766")
logger.info(response)


# token = Token().get(**{
#     "client_id": "37600e6c-e102-40fd-9fb2-1b857111444b",
#     "client_secret": "JCXOONFPEFOEJHXCOPUGGOAOXBAXDSBFKUSTPVDVNRNVIKPPPC",
# }
# )


# o = order(token)
# c = coupon(token)
# l = logistics(token)
# # order_list = o.list(member_phone="13655138366")
# order_list = o.list()
# logger.info(order_list)

# # order_info = o.read("D459632021040917170896244")
# # logger.info(order_info)

# # coupon_list = c.list(member_phone="13801587423")
# # logger.info(coupon_list)

# logistics_info = l.read(tid="D459632021040917170896244")
# logger.info(logistics_info)
