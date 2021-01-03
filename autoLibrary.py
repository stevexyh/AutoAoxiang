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

try:
    import sys
    import json
    import datetime
    import getpass
    import threading
    # import schedule
    import functions.formatString as fs
    import functions.lib_room as lib_room
    from time import sleep
    from functions.loginAoxiang import login_check
    # from functions.getInfo import get_info
except ModuleNotFoundError:
    error_info = '缺少函数库, 运行 pip install -r requirements.txt 命令后重试'
    print(error_info)
    exit(-1)


def log(dic):
    """
    :param dic: log dict(e.g. {name: value})
    """
    res = datetime.datetime.now().strftime('[\033[0;32;1m%y-%m-%d %H:%M:%S\033[0m]') + ' '
    for key in dic:
        flg = dic[key] is not None
        res += format(key, ' <5')
        res += format('\033[0;33;1m' + dic[key] + '\033[0m' if flg else '', ' <30')
    print(res)


def reserve(username, password, room: str = '711', i: int = 0):
    time = lib_room.get_room_time(i)
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
        'start_time': time['start'],
        'end_time': time['end'],
        'up_file': '',
        'memo': '',
        'act': 'set_resv',
        '_': '1609667128663',
    }

    res = conn.post(
        url=urlReserve,
        data=dataReserve,
        headers=header,
    )

    response = {
        'user': username,
        'room': room,
        'time': f"{dataReserve['start_time']}-{dataReserve['end_time']}",
        'msg': json.loads(res.text)['msg'],
    }

    status = '成功' in response['msg']
    log(response) if status else None

    return conn


def init_users():
    with open('./.user_passwd', 'r') as pswd:
        pswd = pswd.readlines()
        user = [{'userid': line.split(',')[0].strip(), 'passwd':line.split(',')[1].strip()} for line in pswd]
    return [threading.Thread(target=reserve, args=[user[i]['userid'], user[i]['passwd'], '711', i]) for i in range(3)]


def start_user(user_list):
    """
    start all users in user_list and join them
    """

    for i in user_list:
        try:
            i.start()
        except AttributeError:
            pass
    for i in user_list:
        try:
            i.join()
        except (AttributeError, RuntimeError):
            pass
    print('-'*30)


if __name__ == '__main__':
    users = init_users()
    start_user(users)

    # name = str(input('学号:'))
    # passwd = str(getpass.getpass('密码:'))

    # reserve(name, passwd)
