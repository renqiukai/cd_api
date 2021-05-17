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
# from cdApi.token_api import Token
import pandas as pd
from loguru import logger
from wowkai_open_api.order import order
from wowkai_open_api.coupon import coupon
from wowkai_open_api.joeone import customer
from wowkai_open_api.token_api import Token
from cdApi.coupon import coupon


token = Token().get(**{
    "client_id": "670473de-3e50-43b0-a098-7b26d5979cb7",
    "client_secret": "YEYXMKYDMLCPVREMKBJPDZSBJAICRQTGMIIGQONTTJDURSQZXT",
}
)

a = customer(token)
response = a.read(member_phone="13761130525")
logger.info(response)
