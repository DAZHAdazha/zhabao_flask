from flask import g


# 登录日志
def login_log():
    print('当前登录用户为：' + g.username)