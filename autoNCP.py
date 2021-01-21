#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
此脚本用于自动填写NCP疫情通报调查表
'''
try:
    import sys
    import datetime
    # import schedule
    import functions.formatString as fs
    from time import sleep
    from functions.loginAoxiang import login_check
    from functions.getInfo import get_info
except ModuleNotFoundError:
    error_info = '缺少函数库, 运行 pip install -r requirements.txt 命令后重试'
    print(error_info)
    exit(-1)


def submitForm(user='', passwd='', loc_code='', loc_name=''):
    '''
    提交表格
    参数: 用户名, 密码, 所在地点
    '''

    session = login_check(user=user, passwd=passwd)

    # 表格url与提交url不同, 否则提交失败
    urlForm = 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'
    urlSubmit = 'http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp'

    # 表格请求头
    formHeaders = {
        'Origin': 'http://yqtb.nwpu.edu.cn',
        'Referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    # 填表信息
    formData = {
        'actionType': 'addRbxx',
        'userLoginId': user,

        # 所在城市编码 / 名称
        'szcsbm': loc_code,
        'szcsmc': loc_name,

        # 是否经停 / 说明
        'sfjt': '0',
        'sfjtsm': '',

        # 是否接触人员 / 说明
        'sfjcry': '0',
        'sfjcrysm': '',

        # 是否接触确诊
        'sfjcqz': '0',

        # 是否有症状
        'sfyzz': '0',

        # 是否确诊 / 异常情况说明
        'sfqz': '0',
        'ycqksm': '',

        # 健康情况 / 说明
        'sfjkqk': '0',
        'jkqksm': '',

        # 隔离情况 / 隔离开始日期 / 隔离结束日期 / tbly和sso是啥意思？？？
        'glqk': '0',
        'glksrq': '',
        'gljsrq': '',
        'tbly': 'sso',

        # 本人承诺(此参数在服务器post里没找到)
        'brcn': '0',
    }

    logData = {
        '所在位置': loc_name,
        '位置编码': loc_code,
        '是否经停湖北': '否',
        '接触湖北籍人员': '否',
        '接触确诊疑似': '否',
        '今日体温': '37.2度以下',
        '有无疑似或异常': '无',
        '您或家属健康状态': '正常',
        '是否隔离': '否',
    }

    print('准备获取表单...')
    session.get(urlForm, timeout=5)

    print('已获取表单, 准备提交...')
    session.post(url=urlSubmit, data=formData, headers=formHeaders, timeout=5)
    res = session.get(urlForm, timeout=5).text
    session.close()

    # 成功信息, 此处为原网页设置, 不可随意更改
    success = '您已成功提交今日上报，重新提交将覆盖上一次的信息。'
    status = res.find('重新提交将覆盖上一次的信息')

    if status != -1:
        print(fs.log_cn(logData))
        print(success)
        print('-' * 100)

        return True
    else:
        print(fs.setColor(string='提交失败, 请重试', color='redBack'))
        print(status)
        return False


if __name__ == "__main__":
    headerInfo = '-' * 100 + '\n' + '''
⚠️  警告: 仅可在确保自身情况正常、信息属实的情况下使用此脚本,一切后果由使用者自己承担,作者概不负责。
⚠️  警告: 若使用者健康情况异常,务必立即停止使用此自动化脚本。
    ''' + '\n' + '-' * 100

    print(headerInfo)

    username, password, location_code, location_name = get_info(is_input=False)

    if 'server' in sys.argv:
        print('`server` arg is no longer available, use crontab in your OS instead.')

    try_time = 3
    while try_time > 0:
        try:
            submitForm(
                user=username,
                passwd=password,
                loc_code=location_code,
                loc_name=location_name
            )

            with open(sys.path[0] + '/autoNCP.log', 'a') as log_file:
                log_file.write(fs.log_line({location_name: 'SUCC'}, color=False)+'\n')

            break

        except Exception as err:
            print(fs.log_line({'提交异常': str(err)}))
            sleep(10)
            try_time -= 1

            with open(sys.path[0] + '/autoNCP.log', 'a') as log_file:
                log_file.write(fs.log_line({'Err:': err}, color=False)+'\n')
