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
    from functions.login_CSU import login_check
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
    urlForm = 'https://wxxy.csu.edu.cn/ncov/wap/default/index'
    urlSubmit = 'https://wxxy.csu.edu.cn/ncov/wap/default/save'

    # 表格请求头
    formHeaders = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'BIGipServerpool_wxxy.csu.edu.cn=2276632768.20480.0000; eai-sess=eu5hcrep5c5q6t06e6til4fb36; UUkey=6cf7b11425d0fe4488b80c915cbee594',
        'Host': 'wxxy.csu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://wxxy.csu.edu.cn/site/applicationSquare/index?sid=1',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }

    # 填表信息
    formData = {
        'jcjgqr': '0',
        'sfjcjwggry': '0',
        'szgjcs': '',
        'szcs': '',
        'szgj': '',
        'sfcysjh': '0',
        'dqszyqfxdj': '',
        'dzjkmys': '',
        'sffx': '1',
        'nj': '2017级',
        'njqt': '',
        'zybj': '交运1703',
        'xslb': '本科生',
        'sfbys': '0',
        'cjtw': '',
        'wjtw': '',
        'wujtw': '',
        'sfywcxyxd': '0',
        'sffdypz': '0',
        'cxsj': '',
        'fxsj': '',
        'cxyy': '',
        'ddd': '',
        'tjd': '',
        'cxjtfs': '',
        'cxjtfsqt': '',
        'ywqtsm': '0',
        'xxqk': '',
        'sfjcyqzgfxdq': '0',
        'sfjtyqzgfxdq': '0',
        'tw': '3',
        'sfcxtz': '0',
        'sfjcbh': '0',
        'sfcxzysx': '0',
        'qksm': '',
        'sfyyjc': '0',
        'remark': '',
        'address': '湖南省长沙市天心区文源街道青年路中南大学铁道学院',
        'geo_api_info': '{"type":"complete","position":{"Q":28.140346137153,"R":112.99368516710103,"lng":112.993685,"lat":28.140346},"location_type":"html5","message":"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.","accuracy":129,"isConverted":true,"status":1,"addressComponent":{"citycode":"0731","adcode":"430103","businessAreas":[{"name":"雨花亭","id":"430111","location":{"Q":28.141963,"R":113.00517500000001,"lng":113.005175,"lat":28.141963}},{"name":"新开铺","id":"430103","location":{"Q":28.135278,"R":112.972872,"lng":112.972872,"lat":28.135278}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"韶山南路","streetNumber":"22号","country":"中国","province":"湖南省","city":"长沙市","district":"天心区","township":"文源街道"},"formattedAddress":"湖南省长沙市天心区文源街道青年路中南大学铁道学院","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
        'area': '湖南省 长沙市 天心区',
        'province': '湖南省',
        'city': '长沙市',
        'sfzx': '1',
        'sfjcwhry': '0',
        'sfjchbry': '0',
        'sfcyglq': '0',
        'gllx': '',
        'glksrq': '',
        'jcbhlx': '',
        'jcbhrq': '',
        'bztcyy': '1',
        'sftjhb': '0',
        'sftjwh': '0',
        'cysjh': '',
        'jcjg': '',
        'date': '20210309',
        'uid': '282216',
        'created': '1615219706',
        'jcqzrq': '',
        'sfjcqz': '',
        'szsqsfybl': '0',
        'sfsqhzjkk': '0',
        'sqhzjkkys': '',
        'sfygtjzzfj': '0',
        'gtjzzfjsj': '',
        'id': '21789456',
        'gwszdd': '',
        'sfyqjzgc': '',
        'jrsfqzys': '',
        'jrsfqzfy': '',
        'ismoved': '0',
    }

    submit_header = {
        'Cache-Control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Date': 'Tue, 09 Mar 2021 16:12:59 GMT',
        'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT',
        'Pragma': 'no-cache',
        'Server': 'dws',
        'Transfer-Encoding': 'chunked',
        'Vary': 'Accept-Encoding',
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'SAMEORIGIN',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '2775',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=175720c7d89362-0e1b75bb654a54-71415a3a-144000-175720c7d8a300; _ga=GA1.3.1031687555.1581936039; eai-sess=f70l9a9cvfv4cp1395nm65gs02; UUkey=cb0f2de43b33858b5872eaee7cfc813d; BIGipServerpool_wxxy.csu.edu.cn=2276632768.20480.0000; Hm_lvt_48b682d4885d22a90111e46b972e3268=1615265057,1615265230,1615265631,1615306096; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1615306096',
        'Host': 'wxxy.csu.edu.cn',
        'Origin': 'https://wxxy.csu.edu.cn',
        'Referer': 'https://wxxy.csu.edu.cn/ncov/wap/default/index',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45',
        'X-Requested-With': 'XMLHttpRequest',
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
    res = session.get(urlForm, headers=formHeaders, timeout=5).text
    if res.find('健康打卡') != -1:
        print('已获取表单, 准备提交...')
    else:
        print('获取表单失败')

    # TODO(Steve X): REMOVE BEFORE FLIGHT
    res = session.post(url=urlSubmit, data=formData, headers=submit_header, timeout=5).text
    # res = session.get(urlForm, timeout=5).text
    session.close()
    print(res)

    # # 成功信息, 此处为原网页设置, 不可随意更改
    # success = '您已成功提交今日上报，重新提交将覆盖上一次的信息。'
    # status = res.find('重新提交将覆盖上一次的信息')

    # if status != -1:
    #     print(fs.log_cn(logData))
    #     print(success)
    #     print('-' * 100)

    #     return True
    # else:
    #     print(fs.setColor(string='提交失败, 请重试', color='redBack'))
    #     print(status)
    #     return False


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
