'''Создать папку'''


import os
from os.path import join


def make_dir(path, dir_name):
    try:
        os.makedirs(join(path, dir_name))
    except FileExistsError:
        print('Can not create dir, because it exists')


make_dir('.', 'testdir')
