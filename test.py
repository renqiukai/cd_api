'''
@Author: Rqk
@Date: 2020-04-26 15:01:20
@Description: 
'''
from cdApi.coupon_pack import couponPack
from cdApi.product import product

if __name__ == "__main__":
    token = "490d3291-c9c6-4792-b11e-f7d9c01960b9"
    c = product(token)
    info = c.read(28710)
    # info["couponList"][0]["number"] = 10
    # print(info)
    info["categoryList"] = [{"id": 1022}, {"id": 2416}, {
        "id": 2420}, {"id": 505}, {"id": 549}, {"id": 550}]
    print(c.update(info))
