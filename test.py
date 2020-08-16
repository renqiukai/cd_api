'''
@Author: Rqk
@Date: 2020-04-26 15:01:20
@Description: 
'''
from cdApi.coupon_pack import couponPack
from cdApi.product import product
from cdApi.store import store

if __name__ == "__main__":
    token = "eee4e7af-74ac-436d-8fb2-87bcd7f305e8"
    s = store(token=token)
    s.update_manager_mobile(29561,"13801234567")
