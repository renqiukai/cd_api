'''
@说明    :订单接口。
@时间    :2020/3/19 下午4:51:48
@作者    :任秋锴
@版本    :1.0
'''

from .base import base


class order(base):
    def __init__(self, token):
        super().__init__(token)

    def list(self, page=1, page_size=10):
        data = {
            "method": "cd.trade.list.get",
            "time": time,
            "pay_stauts": pay_stauts,
            "branch_company_codes": branch_company_codes,
            "member_phone": member_phone,
            "begin_time": begin_time,
            "end_time": end_time,
            "page": page,
            "page_size": page_size,
        }
        return self.request(json=data)

    def sync(self, order_code):
        # 向客户同步销售订单
        api_name = "manager/order/order_invoice"
        data = {"orderCodes": order_code}
        return self.request(api_name, data, method="POST")

    def syncReturn(self, order_code, type=None):
        # 向客户同步售后订单
        api_name = "manager/order/order_invoice"
        data = {"returnCodes": order_code}
        if type:
            data["type"] = type
        return self.request(api_name, data, method="POST")

    def read(self, order_code):
        api_name = "manager/order/info"
        data = {
            "orderCode": order_code,
        }
        response = self.request(api_name, data, method="GET")
        return response

    def bind_order_emp(self, order_code, emp_id):
        # 订单绑定导购方法
        api_name = "manager/order/bind_order_emp"
        data = {
            "orderCode": order_code,
            "empId": emp_id
        }
        response = self.request(api_name, data, method="POST")
        return self.response(response)
