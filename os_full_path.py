'''Склеить путь из папки и файла'''


from os.path import join


def get_full_path(head, trail):
    return join(head, trail)


print(get_full_path('testdir/testsubdir', 'testfile.txt'))
