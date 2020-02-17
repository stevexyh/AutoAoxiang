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
        res += ('\033[0;33;1m' + dic[key] + '\033[0m' if flg else '').ljust(20,chr(12288)) + '\n'
    print(res)



def log_cn(dic):
    """
    中文多行log
    :param dic: log dict(e.g. {name: value})
    """
    formLen = 40

    res = '-' * formLen + '\n'
    res += datetime.datetime.now().strftime('[\033[0;32;1m%Y-%m-%d %H:%M:%S\033[0m]') + '\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(12,chr(12288))
        res += ('\033[0;33;1m' + dic[key] + '\033[0m' if flg else '').ljust(20,chr(12288)) + '\n'
    res += '-' * formLen
    print(res)


def log_en(dic):
    """
    英文log
    :param dic: log dict(e.g. {name: value})
    """
    formLen = 40

    res = '-' * formLen + '\n'
    res += datetime.datetime.now().strftime('[\033[0;32;1m%Y-%m-%d %H:%M:%S\033[0m]') + '\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(20)
        res += ('\033[0;33;1m' + dic[key] + '\033[0m' if flg else '').ljust(20) + '\n'
    res += '-' * formLen
    print(res)


def setColor(string, color):
    if color == 'redFore':
        return colorama.Fore.RED+ colorama.Back.RESET + string + colorama.Style.RESET_ALL
    elif color == 'redBack':
        return colorama.Fore.WHITE+ colorama.Back.RED + string + colorama.Style.RESET_ALL
    elif color == 'greenFore':
        return colorama.Fore.GREEN+ colorama.Back.RESET + string + colorama.Style.RESET_ALL
    elif color == 'greenBack':
        return colorama.Fore.BLACK+ colorama.Back.GREEN + string + colorama.Style.RESET_ALL

# if __name__ == "__main__":
#     a = 'This is red.'
#     b = setColor(a, 'redFore')
#     print(b)

#     log_cn(logData)