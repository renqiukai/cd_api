'''
@说明    :订单接口。
@时间    :2020/3/19 下午4:51:48
@作者    :任秋锴
@版本    :1.0
'''

from .base import base
import time
from loguru import logger


class coupon(base):
    def __init__(self, token):
        super().__init__(token)

    def list(self,
             data_type=1,
             member_phone=None):
            # https://opendoc.icaodong.com/2020/02/27/adapter-caodong/#No-3-1-%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8
            # data_type:1-会员优惠券 2-门店优惠券
        data = {
            "method": "cd.coupon.list.get",
            "time": self.time,
            "data_type": data_type,
        }
        if member_phone:
            data["member_phone"] = member_phone
        # logger.debug(data)
        return self.request(method="POST", json=data)

    def read(self,
             tid,
             branch_company_codes=None):
            # https://opendoc.icaodong.com/2020/02/27/adapter-caodong/#No-3-1-%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8
            # pay_stauts:PAY_NO-未付款 PAY_FINISH-已付 REFUND_ALL-全额退款
        data = {
            "method": "cd.trade.fullinfo.get",
            "time": self.time,
            "tid": tid,
        }
        if branch_company_codes:
            data["branch_company_codes"] = branch_company_codes
        # logger.debug(data)
        return self.request(method="POST", json=data)
