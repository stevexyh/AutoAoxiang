#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import colorama

logData = {
    '所在位置': '北京',
    '是否经停湖北': '否',
    '接触湖北籍人员': '否',
    '接触确诊疑似': '否',
    '今日体温': '37.2度以下',
    '有无疑似或异常': '无',
    '是否隔离': '否',
}


def log_line(dic):
    """
    中文单行log
    :param dic: log dict(e.g. {name: value})
    """

    for key in dic:
        flg = dic[key] is not None
        res = str(key).ljust(12,chr(12288))
        res += (setColor(dic[key], color = 'yellowFore') if flg else '').ljust(20,chr(12288)) + '\n'
    print(res)



def log_cn(dic):
    """
    中文多行log
    :param dic: log dict(e.g. {name: value})
    """
    formLen = 40

    res = '-' * formLen + '\n'
    res += '[' + setColor(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), color = 'greenFore') + ']\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(12,chr(12288))
        res += (setColor(dic[key], color = 'yellowFore') if flg else '').ljust(20,chr(12288)) + '\n'
    res += '-' * formLen
    print(res)


def log_en(dic):
    """
    英文log
    :param dic: log dict(e.g. {name: value})
    """
    formLen = 40

    res = '-' * formLen + '\n'
    res += '[' + setColor(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), color = 'greenFore') + ']\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(20)
        res += (setColor(dic[key], color = 'yellowFore') if flg else '').ljust(20) + '\n'
    res += '-' * formLen
    print(res)


def setColor(string, color):
    convertColor = {
        'redFore': colorama.Fore.RED + colorama.Back.RESET, 
        'redBack': colorama.Fore.WHITE + colorama.Back.RED,

        'greenFore': colorama.Fore.GREEN + colorama.Back.RESET,
        'greenBack': colorama.Fore.BLACK + colorama.Back.GREEN,

        'yellowFore': colorama.Fore.YELLOW + colorama.Back.RESET,
    }

    return colorama.Style.BRIGHT + convertColor[color] + string + colorama.Style.RESET_ALL


if __name__ == "__main__":
    a = 'This is red.'
    b = setColor(a, 'redFore')
    print(b)

    log_cn(logData)