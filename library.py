#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
----------------------------------------------------------------------------------------------------
* Project Name : AutoAoxiang
* File Name    : library.py
* Description  : 
* Create Time  : 2021-03-13 01:35:08
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh/AutoAoxiang
----------------------------------------------------------------------------------------------------
* Notice
- 
- 
----------------------------------------------------------------------------------------------------
'''


import requests


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '2249',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '__AntiXsrfToken=8880d617640b4621b33ef352fc2c048f',
    'Host': 'yy.lib.neau.edu.cn',
    'Origin': 'http://yy.lib.neau.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://yy.lib.neau.edu.cn/dgyy/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}

data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': 'KoaCBnSIqGJvZ++fX5kOY7d1e5oamfHVJulHURw/VcR+PfgUIkj5rHsXwmD+0gFTlGAjXbUG96lI2uFU+17Z8XygBBZkT6mxfgF7kQNS4jWdgM/dbKYOMCQsRaKjqgsOTX8VM+jAqYEUIuTNvWvcXJPRGz/qvCC9SLjL1vVTjaIxW60L8dKP+n7xnXLOcehYs7lraYvNdVhGpJRYCfwogtjKhyicYj0f9FMj6c9gJnAq7rbdvxyUQPV2VULsjDGhAdqTWQxcguLWDamhztBxFZT8wk6COKZjWyjourRC/Naum+QqPc//mtkNQ16Elti00JtYDUyZSJ6n2T1ngjv00+GgzZJxuRvWuw0GlenIjltfKnFLLFBydCzcNUXxCRn7YBM+TGi39mkgN094PRWUOmUWbNnOao7+VKOsN9PJLsiUgyFl/7MS4a9/wIBSA0Y3lD0/pDF+z1m08NmdseP8nAMYdUpxDgh/8Ixmn0pkubvK2tEuxPmjai17BwLPqgrOC5bO40DVwHqoz5qrme9+v0xXApgACxO592PoD6aQn3nvK0Y5/ljrGXLEEX3mGJmhfaiHwNw4tQz8+lRgBjiC8E2Y3YuZR//tgOYJ8BdEHfg=',
    '__VIEWSTATEGENERATOR': 'F0E8140F',
    '__EVENTVALIDATION': 'Yohn6PhX8Ntd5L40BtydYqLTlgiYTJRXn/N3AgVpvNJnkjUpVthGqFjJ/MXL7sFh6m+zAXyB8UdqDvkSMS3X9PkBHKjUI3gtNgrNrWV+cCWIjtZPZ7JeeXuYEp/U6jsC9tdeH+j+J0zK1xyknKhObyLGc+s52/w0L21hf0XMjDuQeVFuy4dKuFlCvUxPsP5ORS//L5WLzNAIf4gXBHz18s6teLmVi6ge3V4TupwMIld6OVw7buPUKZ1ymZRtHwkt8IP9G+CTs+fsaxwvX5Mc3dHkPTqVc9fY6Mxh4UuX/cyXAFZwyfSmSmYGxeKtzPPdW6zjEI70D551hGsXGTXHiBANOSGQAznl/qv4ZZ52VTiYRptMq6yMYaEOMlfbdO35fxA8EtYrW0neGn3wkUE22tcKlHW94k2HVijlOkJqlQqY0MHmdcyPXf8RKk70wf+oEkCwLL0Uz2gVvsbzXEG9R0rv/xyPLGBj44YbzPOmxtfs2yaAWKsfajE806LeU9gG9mrVR6f/fAh25nZSzqcN2qo5Naq79kWroNO2KhyXtXtJ5TiFfueJix3z1TcmxBuykNEKXlQBdrImEgdRkNfvDQJgeeAE8ocHGRlsVrc9GB9L3l27W2rUX2eqC8SVF8utRaVtlgAWjo9XGXRQTmtu/PI56w9yMf2ABreUjzAk2dxT3I2M8yxhCoktAlbZSEqcQrNlUxIq/Meh97RJgoD4qrmkhiTcYwn5k76J26BTjFqac3+B7X0zlxbeYKgKOi9BF3k2wNlpgkkRxle43gmwi20lANMJ8B89bpuwtdyssKLWgV3QCOL8jdkq6sicm+O5lKAk35HyHNxH8PxQbGZNCabwn2FygOhORWbP0zd5MScb2RS3Mx5ygVlOIsqbgjzqfimYduM/at81aFTwYSJ+sWObji9m9ozd501eGXNp3WimLpc5koj3TpVMAXM/q+n7DkmYVwyn6nNea1A5CrgpJC9DrsMcZYlZtnPX+0OrDw5gKuWI2lBnKcMXwDhu/YsG4G186tTLAhdRyyU/7pL4VuynIIIaD+EVxCgw/tnecxKr48tgUeyKw7OyRlpU6VvQ/S2AGtUhCwx7RUqu8d4P5ZtApdTw/4wYdQN6kRUGBSU1YQN0BTiGL5Z2fzUhXz/pIyT5l/7nmGdyYAIYoRoTvTKqs0zNdFhLamZ+bHmaUX0=',
    'ctl00$MainContent$TextBox1': 'A07170123',
    'ctl00$MainContent$TextBox2': '090215',
    'ctl00$MainContent$TextBox3': '18800432181',
    'ctl00$MainContent$TextBox4': '学',
    'ctl00$MainContent$YuYue': '预约',
}

def run():
    session = requests.Session()
    res = session.post(url='http://yy.lib.neau.edu.cn/dgyy/',headers=headers, data=data).text
    status = '当前已经预约了' if '当前已经预约了' in res else '应该约上了'
    print(status)


if __name__ == "__main__":
    run()
