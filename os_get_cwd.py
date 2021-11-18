'''Получить текущую директорию'''


import os


def get_current_dir():
    return os.getcwd()


if __name__ == "__main__":
    print(get_current_dir())
