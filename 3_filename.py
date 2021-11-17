'''Дана строка, содержащая полное имя файла (например, C:\development\inside\test-
project_management\inside\myfile.txt'). Выделите из этой строки имя файла без расширения'''


def get_filename(path):

    return path.split('\\')[-1].split('.')[0]


print(get_filename(r'C:\development\inside\test-project_management\inside\myfile.txt'))
