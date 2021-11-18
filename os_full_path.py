'''Склеить путь из папки и файла'''

import os
from os.path import join


def get_full_path(head, trail):
    return join(head, trail)


print(get_full_path(f'testdir{os.sep}testsubdir', 'testfile.txt'))
