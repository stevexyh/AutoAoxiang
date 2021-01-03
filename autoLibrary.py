#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : AutoAoxiang
* File Name    : autoLibrary.py
* Description  : Reserve library room automatically.
* Create Time  : 2021-01-03 18:39:37
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/AutoAoxiang
----------------------------------------------------------------------------------------------------
* Notice
- 
- 
----------------------------------------------------------------------------------------------------
'''

import getpass
try:
    import sys
    import datetime
    # import schedule
    import functions.formatString as fs
    from time import sleep
    from functions.loginAoxiang import login_check
    # from functions.getInfo import get_info
except ModuleNotFoundError:
    error_info = '缺少函数库, 运行 pip install -r requirements.txt 命令后重试'
    print(error_info)
    exit(-1)


def reserve(username, password):
    conn = login_check(username, password)
    urlReserve = 'http://202.117.88.170/ClientWeb/pro/ajax/reserve.aspx'
    # urlReserve = 'http://202.117.88.170/ClientWeb/pro/ajax/reserve.aspx?dialogid=&dev_id=857229&lab_id=857069&kind_id=959784&room_id=&type=dev&prop=&test_id=&term=&number=&classkind=&test_name=curltest&min_user=2&max_user=8&mb_list=2017302341%2C2017302342&start=2021-01-05+08%3A30&end=2021-01-05+09%3A29&start_time=830&end_time=929&up_file=&memo=&act=set_resv&_=1609667128663'

    header = {
        # 'Origin': 'https://uis.nwpu.edu.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ASP.NET_SessionId=lj3jbjbsktusf0t1fpzpy4yo',
        'Host': '202.117.88.170',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://202.117.88.170/ClientWeb/xcus/ic2/Default.aspx',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }

    dataReserve = {
        'dialogid': '',

        # 房间号
        'dev_id': '857229',
        'lab_id': '857069',
        'kind_id': '959784',
        'room_id': '',
        'type': 'dev',
        'prop': '',
        'test_id': '',
        'term': '',
        'number': '',
        'classkind': '',

        # 房间主题
        'test_name': 'fakehhhhhh',
        'min_user': '2',
        'max_user': '8',

        # 学号
        'mb_list': '2017302342,2017302341',

        # 时间
        'start': '2021-01-05 08:30',
        'end': '2021-01-05 09:29',
        'start_time': '0830',
        'end_time': '0929',
        'up_file': '',
        'memo': '',
        'act': 'set_resv',
    }

    res = conn.post(
        url=urlReserve,
        data=dataReserve,
        headers=header,
    )
    print(res.url)
    print(res)
    print(res.text)
    return conn


if __name__ == '__main__':
    name = str(input('学号:'))
    passwd = str(getpass.getpass('密码:'))

    reserve(name, passwd)
