'''Получить список файлов в папке'''


from os import listdir
from os.path import isfile, join


def show_dir_files(dir_name):
    return [f for f in listdir(dir_name) if isfile(join(dir_name, f))]


print(show_dir_files('.'))
