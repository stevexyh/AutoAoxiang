#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
此脚本用于自动填写NCP疫情通报调查表
'''

import getpass
from urllib import parse
from functions.loginAoxiang import login

def submitForm(user = '', passwd = '', location = ''):
    '''
    提交表格
    参数: 用户名, 密码, 所在地点
    '''

    session, status = login(user = user, passwd = passwd)
    if status == False:
        exit(-1)

    urlForm = 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'

    #表格请求头
    formHeaders = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://yqtb.nwpu.edu.cn',
        'Referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp',
    }

    #填表信息
    formData = {
        'actionType': 'addRbxx',
        'userLoginId': user,

        #所在城市编码 / 名称
        'szcsbm': 3,
        'szcsmc': parse.quote(str(input('地点:'))),

        #是否经停 / 说明
        'sfjt': 0,
        'sfjtsm': '',
        
        #是否接触人员 / 说明
        'sfjcry': 0,
        'sfjcrysm': '',
        
        #是否接触确诊
        'sfjcqz': 0,

        #是否有症状
        'sfyzz': 0,

        #是否确诊 / 异常情况说明
        'sfqz': 0,
        'ycqksm': '',

        #隔离情况 / 隔离开始日期 / 隔离结束日期 / tbly和sso是啥意思？？？
        'glqk': 0,
        'glksrq': '',
        'gljsrq': '',
        'tbly': 'sso',
    }

    res = session.post(url = urlForm, data = formData, headers = formHeaders).text
    success = '您已成功提交今日上报，重新提交将覆盖上一次的信息'
    status = res.find(success) != -1

    if status:
        print(success)
    else:
        print('提交失败, 请重试')
        print(res)


if __name__ == "__main__":
    username = str(input('学号:'))
    password = str(getpass.getpass('密码:'))

    submitForm(user = username, passwd = password)