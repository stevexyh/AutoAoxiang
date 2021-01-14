import getpass
import os
from .location import get_location_info

cache_file = '.cache_info'


def get_info(is_input=True):
    '''
    获取登录所需信息

    #### Parameters::
        is_input = True  - 手动输入信息
        is_input = False - 从缓存文件读取信息

    #### Returns::
        user_name, password, location_code, location_name
    '''
    if is_input:
        user_name = input("学号:__________\b\b\b\b\b\b\b\b\b\b")
        password = getpass.getpass('密码:')
        # location = input("地点:__________\b\b\b\b\b\b\b\b\b\b")

        is_school = bool(int(input("是否在学校(是1/否0):_\b")))
        if is_school:
            location_code = '1'
            location_name = '在学校'
        else:
            location = get_location_info()
            location_code = location['full_code']
            location_name = location['full_name']
    else:
        try:
            user_name, password, location_code, location_name = open(cache_file).read().split('\n')
        except (FileNotFoundError, ValueError):
            remove_cache()
            return write_info()
    return user_name, password, location_code, location_name


def write_info():
    username, password, location_code, location_name = get_info(is_input=True)
    with open(cache_file, 'w') as f:
        f.write(username + '\n' + password + '\n' + location_code + '\n' + location_name)
        return username, password, location_code, location_name


def remove_cache():
    try:
        os.remove(cache_file)
    except FileNotFoundError:
        pass
