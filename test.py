'''
@Author: Rqk
@Date: 2020-04-26 15:01:20
@Description: 
'''
from logging import log
from cdApi.coupon_pack import couponPack
from cdApi.product import product
from cdApi.user import user
import pandas as pd
from loguru import logger

if __name__ == "__main__":
    token = "88b81d1a-c412-4e83-9740-690e8811d6c3"
    s = user(token=token)
    filename = "C:\\Users\\renqi\\CloudStation\\我的工作\\桌面\\只有手机号码用户(1).xls"
    df = pd.read_excel(filename)
    idList = []
    for idx, mobile in enumerate(df["手机号码"], start=1):
        users = s.list(mobile=mobile)
        users = users.get("data")
        totalCount = users.get("totalCount")
        # print(users)
        if totalCount:
            users = users.get("dataList")
            user = users[0]
            user_id = user.get("id")
            idList.append(user_id)
            logger.success({"idx": idx, "mobile": mobile, "user_id": user_id})
        else:
            logger.error({"idx": idx, "mobile": mobile})
        if len(idList) % 50 == 0 and len(idList) > 0:
            result = s.batch_delete(idList=idList)
            logger.success({"result": result, "idList": idList})
            idList = []
            # break
