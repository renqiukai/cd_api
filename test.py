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
from wowkai_open_api.order import order
from wowkai_open_api.coupon import coupon
from wowkai_open_api.logistics import logistics
from wowkai_open_api.token_api import Token


# token = "59beb8f8-137f-4c0f-a1ef-03d1fbe6ab35"
# a = auth(token)
# response = a.update_status(_id="21844", status=1)
# logger.info(response)


token = Token().get(**{
    "client_id": "dcba689c-919a-11ea-896d-02425e922344",
    "client_secret": "DPRBGOHEOHNDTXQBFRAYPUTDZGTJQLAFSYFUKNYTTWGFMKKA",
}
)


o = order(token)
c = coupon(token)
l = logistics(token)
# order_list = o.list(member_phone="13655138366")
order_list = o.list()
logger.info(order_list)

# order_info = o.read("D459632021040917170896244")
# logger.info(order_info)

# coupon_list = c.list(member_phone="13801587423")
# logger.info(coupon_list)

logistics_info = l.read(tid="D459632021040917170896244")
logger.info(logistics_info)
