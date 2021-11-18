'''Посчитать сколько в каталоге установки python:
• папок
• файлов с расширением ".py"
• файлов с расширением ".exe"
• всего файлов
• Записать результаты в файл '''


import sys
import os


def write_files_count(start_path=None):
    with open('files_count.txt', 'w', encoding='utf-8') as fc:
        dirpath, dirnames, filename = next(os.walk(start_path))

        fc.write(f'Папок: {len(dirnames)}\n')
        fc.write(f'Файлов с расширением ".py": {len([x for x in filename if x.endswith(".py")])}\n')
        fc.write(f'Файлов с расширением ".exe": {len([x for x in filename if x.endswith(".exe")])}\n')
        fc.write(f'Всего файлов: {len(filename)}\n')


write_files_count(sys.path[-1])
