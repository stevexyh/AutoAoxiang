#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import getpass
from bs4 import BeautifulSoup
from . import formatString

def getToken(url):
    '''
    获取网页token
    返回token, session
    '''

    session = requests.Session()
    res = session.get(url).text
    token = BeautifulSoup(res, 'html.parser').find(
        name = 'input', 
        attrs = {
            'name' : 'lt'
        }
    ).get('value')

    return token, session


def login(user = '', passwd = '', urlLogin = 'https://uis.nwpu.edu.cn/cas/login'):
    '''
    登录post
    返回session, 登录状态status
    '''

    token, session = getToken(urlLogin)

    #登录页请求头
    header = {
        'Origin': 'https://uis.nwpu.edu.cn',
        'Referer': urlLogin,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    #登录信息
    loginData = {
        'username': user,
        'password': passwd,
        'lt': token,
        '_eventId': 'submit',
    }

    res = session.post(url = urlLogin, data = loginData, headers = header).text
    status = res.find('登录成功') != -1

    if status:
        print(formatString.setColor(string = '登录成功√', color = 'greenFore'))
        status = 1
    else:
        if res.find('密码错误') != -1:
            print(formatString.setColor(string = '密码错误, 请重试', color = 'redBack'))
            status = -1
        else:
            # print(res)
            print(formatString.setColor(string = '密码正确, 登录失败, 准备重新登录...', color = 'redBack'))
            status = 0

    return session, status

# if __name__ == "__main__":
#     username = str(input('学号:'))
#     password = str(getpass.getpass('密码:'))

#     login(user = username, passwd = password)
