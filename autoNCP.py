#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
此脚本用于自动填写NCP疫情通报调查表
'''
try:
    import getpass
    import datetime
    # import schedule
    import functions.formatString as fs
    from time import sleep
    from urllib import parse
    from functions.loginAoxiang import login_check
    from functions.getInfo import remove_cache, get_info
except ModuleNotFoundError:
    error_info = '缺少函数库, 运行 pip install -r packages.txt 命令后重试'
    print(error_info)
    exit(-1)


def submitForm(user = '', passwd = ''):
    '''
    提交表格
    参数: 用户名, 密码, 所在地点
    '''

    session = login_check(user = user, passwd = passwd)

    #表格url与提交url不同, 否则提交失败
    urlForm = 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'
    urlSubmit = 'http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp'
    global location

    if location == '':
        location = str(input('地点:'))

    #表格请求头
    formHeaders = {
        'Origin': 'http://yqtb.nwpu.edu.cn',
        'Referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    #填表信息
    formData = {
        'actionType': 'addRbxx',
        'userLoginId': user,

        #所在城市编码 / 名称
        'szcsbm': '3',
        'szcsmc': location,

        #是否经停 / 说明
        'sfjt': '0',
        'sfjtsm': '',

        #是否接触人员 / 说明
        'sfjcry': '0',
        'sfjcrysm': '',
        
        #是否接触确诊
        'sfjcqz': '0',

        #是否有症状
        'sfyzz': '0',

        #是否确诊 / 异常情况说明
        'sfqz': '0',
        'ycqksm': '',

        #隔离情况 / 隔离开始日期 / 隔离结束日期 / tbly和sso是啥意思？？？
        'glqk': '0',
        'glksrq': '',
        'gljsrq': '',
        'tbly': 'sso',

        #本人承诺(此参数在服务器post里没找到)
        'brcn': '0',
    }

    logData = {
        '所在位置': location,
        '是否经停湖北': '否',
        '接触湖北籍人员': '否',
        '接触确诊疑似': '否',
        '今日体温': '37.2度以下',
        '有无疑似或异常': '无',
        '是否隔离': '否',
    }

    print('准备获取表单...')
    session.get(urlForm)

    print('已获取表单, 准备提交...')
    session.post(url = urlSubmit, data = formData, headers = formHeaders)
    res = session.get(urlForm).text
    session.close()

    #成功信息, 此处为原网页设置, 不可随意更改
    success = '您已成功提交今日上报，重新提交将覆盖上一次的信息。'
    status = res.find(success)

    if status != -1:
        fs.log_cn(logData)
        print(success)

        global post_time, hrs
        post_time = datetime.datetime.now()
        next_post = post_time + datetime.timedelta(hours = hrs)
        next_dict = {'下次提交时间:': next_post.strftime('%Y-%m-%d %H:%M:%S')}
        fs.log_line(next_dict)
        print('-' * 100)

        return True
    else:
        print(fs.setColor(string = '提交失败, 请重试', color = 'redBack'))
        print(status)
        return False


if __name__ == "__main__":
    headerInfo = '-' * 100 + '\n' + '''
⚠️  警告: 仅可在确保自身情况正常、信息属实的情况下使用此脚本,一切后果由使用者自己承担,作者概不负责。
⚠️  警告: 若使用者健康情况异常,务必立即停止使用此自动化脚本。
    ''' + '\n' + '-' * 100

    print(headerInfo)

    username, password, location = get_info(is_input = False)
    hrs = input('定时运行间隔时间(单位: 小时, 默认1):')
    hrs = 1 if hrs == '' else float(hrs)

    while True:
        submitForm(user = username, passwd = password)
        sleep(hrs * 3600)