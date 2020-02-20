import getpass
import os

cache_file = '.cache_info'


def get_info(is_input=True):
    if is_input:
        user_name = input("学号:__________\b\b\b\b\b\b\b\b\b\b")
        password = getpass.getpass('密码:')
        location = input("地点:__________\b\b\b\b\b\b\b\b\b\b")
    else:
        try:
            user_name, password, location = open(cache_file).read().split('\n')
        except FileNotFoundError:
            return prepare()
    return user_name, password, location


def prepare():
    userName, password, location = get_info(is_input=True)
    with open(cache_file, 'w') as f:
        f.write(userName + '\n' + password + '\n' + location)
        return userName, password, location


def remove_cache():
    try:
        os.remove(cache_file)
    except FileNotFoundError:
        pass

