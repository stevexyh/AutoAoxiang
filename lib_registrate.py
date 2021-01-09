#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : AutoAoxiang
* File Name    : lib_registrate.py
* Description  : 自动签到
* Create Time  : 2021-01-09 14:26:53
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/AutoAoxiang
----------------------------------------------------------------------------------------------------
* Notice
- 
- 
----------------------------------------------------------------------------------------------------
'''

# TODO(Steve X): 自动签到没写完

import requests

conn = requests.Session()

url = 'http://update.unifound.net/wxnotice/s.aspx?c=3_indoor_1028_1CD'
# url_msg = 'http://iroom.nwpu.edu.cn/Pages/WxOpenDoorMsg.aspx'
url_login = 'http://iroom.nwpu.edu.cn/Pages/WxOpenDoor.aspx'
data = {
    'DoLogon': 'true',
    'szLogonName': '',
    'szPassword': '',
    'dwBind': '1',
}

# conn.get(url_login)
res = conn.post(
    url=url,
    data=data,
)

data_reg = '?type=1&title=开门成功&msg=该号与帐号绑定成功开门成功&msg2='

print(res.text)

# res = conn.get(url+data_reg)
# print(url+data_reg)
# print(res.text)
