'''
@Author: Rqk
@Date: 2020-04-26 15:01:20
@Description: 
'''
from cdApi.coupon_pack import couponPack

if __name__ == "__main__":
    token = "6733e135-9db9-4ca3-9b57-b06d18fbc5d5"
    c = couponPack(token)
    info = c.read(170)
    info["couponList"][0]["number"] = 10
    print(info)
    print(c.update(info))
