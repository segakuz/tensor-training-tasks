'''Склеить путь из папки и файла'''

import os
import re
from os.path import join, normpath


def get_full_path(head, trail):
    normalized_head = f'{os.sep}'.join(re.split(r'[/\\]+', head))

    return normpath(join(normalized_head, trail))


if __name__ == "__main__":
    print(get_full_path('\\different/slashes', 'testfile.txt'))
