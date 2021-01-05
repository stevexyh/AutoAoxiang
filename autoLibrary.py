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

# DEBUG = True
DEBUG = False
#DEBUG = True

try:
    import sys
    import json
    import datetime
    import getpass
    import threading
    import argh
    # import schedule
    import functions.formatString as fs
    import functions.lib_room as lib_room
    import functions.loginAoxiang as aoxiang
    from time import sleep
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
    room = lib_room.get_room(room)
    now = datetime.datetime.now()
    now_time = int(now.strftime('%H%M'))
    reserve_date = (now+datetime.timedelta(days=2, minutes=10)).strftime('%Y-%m-%d')
    url_reserve = 'http://202.117.88.170/ClientWeb/pro/ajax/reserve.aspx'

    conn, status = aoxiang.login(username, password, url_login='https://uis.nwpu.edu.cn/cas/login?service=http://202.117.88.170/loginall.aspx')
    res = conn.get(url=url_reserve)
    session_id = conn.cookies.get_dict().get('ASP.NET_SessionId')
    print(res.text)
    print('SSID:'+str(session_id))

    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'ASP.NET_SessionId=uiwirsdqtscke3qhdpmgnkwy',
        'Cookie': 'ASP.NET_SessionId='+str(session_id),
        'Host': '202.117.88.170',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://202.117.88.170/ClientWeb/xcus/ic2/Default.aspx',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }

    data_reserve = {
        'dialogid': '',

        # 房间号
        'dev_id': room['dev_id'],
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
        'test_name': f'学{i+1}',
        'min_user': '2',
        'max_user': '8',

        # 学号
        'mb_list': ','.join(user_id),

        # 时间
        'start': f"{reserve_date} {time['start'][:2]}:{time['start'][-2:]}",
        'end': f"{reserve_date} {time['end'][:2]}:{time['end'][-2:]}",
        'start_time': time['start'],
        'end_time': time['end'],
        'up_file': '',
        'memo': '',
        'act': 'set_resv',
    }

    while True:
        if 2358 <= now_time or now_time <= 15 or DEBUG:
            res = conn.post(
                url=url_reserve,
                data=data_reserve,
                headers=header,
            )

            response = {
                f'{username}: ': room['name'] + f"[{data_reserve['test_name']}]",
                # 'date': reserve_date,
                reserve_date: f"({data_reserve['start_time']}-{data_reserve['end_time']})",
                'msg': json.loads(res.text)['msg'] if res.ok else 'FAILED',
            }

            status = '成功' in response['msg']
            if status or DEBUG:
                log(response)

            sleep(2)


def init_users(user: dict):
    return [threading.Thread(target=reserve, args=[u['userid'], u['passwd'], '717', i]) for i, u in enumerate(user)]


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
    with open('./.user_passwd', 'r') as pswd:
        pswd = pswd.readlines()
        user = [{'userid': line.split(',')[0].strip(), 'passwd':line.split(',')[1].strip()} for line in pswd]
        user_id = [u['userid'] for u in user]

    parser = argh.ArghParser(description='Library Reservation')
    parser.dispatch()

    users_init = init_users(user)
    start_user(users_init)
