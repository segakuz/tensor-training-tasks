'''Склеить путь из папки и файла'''


from os.path import join
from os_get_cwd import get_current_dir


def get_full_path(head, trail):
    return join(head, trail)


if __name__ == "__main__":
    print(get_full_path(get_current_dir(), 'testfile.txt'))
