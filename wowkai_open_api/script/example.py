'''
缓存TOKEN
'''
import time
import sqlite3
from loguru import logger
# from app.core.config import CLIENT_ID, CLIENT_SECRET
from wowkai_open_api.token_api import Token

CLIENT_ID, CLIENT_SECRET = "test", "test"
connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()


def save_token_info():
    t = Token()
    data = t.get_info(CLIENT_ID, CLIENT_SECRET)
    token = data.get("data").get("access_token")
    expires_in = data.get("data").get("expires_in")
    timestamp = int(time.time())
    sql = f"""
    insert into t_token
    values('{token}','{timestamp}','{timestamp+expires_in}');
    """
    cursor.execute(sql)
    connection.commit()
    logger.debug(sql)


def get_token():
    """get_token
    判断是否有token记录：
    无：
    1，请求token。
    2，保存创建时间和过期时间。
    有：
    1，检查是否过期
    1.1，过期重新申请，保存。
    1.2，非过期直接使用。
    """
    sql = f"""
    select * from t_token
    order by expires_time desc
    limit 1
    ;
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    if rows:
        row = rows[0]
        timestamp = int(time.time())
        expires_time = row[2]
        if timestamp >= expires_time:
            # 过期，重新申请
            save_token_info()
    else:
        # 没有记录，重新申请
        save_token_info()
    cursor.execute(sql)
    rows = cursor.fetchall()
    row = rows[0]
    return row
