#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : Auto_CSU
* File Name    : room.py
* Description  : Room info
* Create Time  : 2021-01-03 18:39:27
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/Auto_CSU
----------------------------------------------------------------------------------------------------
* Notice
-
-
----------------------------------------------------------------------------------------------------
'''

import random

room_2 = {
    '705': {
        'dev_id': '857207',
        'name': '研修间2(705)',
        'num': 2,
    },
    '706': {
        'dev_id': '857211',
        'name': '研修间3(706)',
        'num': 2,
    },
    '707': {
        'dev_id': '857216',
        'name': '研修间4(707)',
        'num': 2,
    },
    '708': {
        'dev_id': '857220',
        'name': '研修间5(708)',
        'num': 2,
    },
    '709': {
        'dev_id': '857225',
        'name': '研修间6(709)',
        'num': 2,
    },
    '710': {
        'dev_id': '857229',
        'name': '研修间7(710)',
        'num': 2,
    },
    '711': {
        'dev_id': '857235',
        'name': '研修间8(711)',
        'num': 2,
    },
    'rand_start': 705,
    'rand_end': 711,
}

room_4 = {
    '712': {
        'dev_id': '1497787',
        'name': '研修间9(712)',
        'num': 4,
    },
    '713': {
        'dev_id': '1497791',
        'name': '研修间10(713)',
        'num': 4,
    },
    '714': {
        'dev_id': '1497801',
        'name': '研修间11(714)',
        'num': 4,
    },
    '715': {
        'dev_id': '1497806',
        'name': '研修间12(715)',
        'num': 4,
    },
    '716': {
        'dev_id': '1497810',
        'name': '研修间13(716)',
        'num': 4,
    },
    '717': {
        'dev_id': '1497814',
        'name': '研修间14(717)',
        'num': 4,
    },
    '718': {
        'dev_id': '1497884',
        'name': '研修间15(718)',
        'num': 4,
    },
    '719': {
        'dev_id': '1497892',
        'name': '研修间16(719)',
        'num': 4,
    },
    '720': {
        'dev_id': '1497896',
        'name': '研修间17(720)',
        'num': 4,
    },
    '721': {
        'dev_id': '1497937',
        'name': '研修间18(721)',
        'num': 4,
    },
    '722': {
        'dev_id': '1497949',
        'name': '研修间19(722)',
        'num': 4,
    },
    '723': {
        'dev_id': '1497945',
        'name': '研修间20(723)',
        'num': 4,
    },
    '724': {
        'dev_id': '1497941',
        'name': '研修间21(724)',
        'num': 4,
    },
    'rand_start': 712,
    'rand_end': 724,
}


room_time = [
    {
        'start': '1030',
        'end': '1330',
        'name': '上午',
    },
    {
        'start': '1359',
        'end': '1659',
        'name': '下午',
    },
    {
        'start': '1820',
        'end': '2120',
        'name': '晚上',
    },
]


def get_room_time(i):
    '''
    Parameters::
        i - thread id
    Returns::
        {
            'start',
            'end',
            'name',
        }
    '''

    return room_time[i % len(room_time)]


def get_room(room: str = '705', num: int = 4, rand_room: bool = False) -> str:
    '''
    descriptions

    Parameters::
        room: int - room No.
        num: int - 2 / 4
        rand_room: bool - whether choose room randomly
    Returns::
        room: dic - {
            'dev_id' - room ID,
            'name' - room name,
            'num' - min num of room,
        }
    '''

    num = 2 if (num == 2 or num & 1) else 4
    room_dic = room_2 if num == 2 else room_4

    if rand_room:
        start = room_dic['rand_start']
        end = room_dic['rand_end']
        rand_id = str(random.randint(start, end))
        return room_dic[rand_id]

    return room_dic[room]


if __name__ == "__main__":
    res = get_room(
        room='711',
        num=4,
        rand_room=True,
    )

    print(res)
