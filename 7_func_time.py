'''Напишите декоратор func_time, который подсчитывает и выводит сколько времени выполняется
функция, обернутая в него.
@func_time
def some_func():
   # some_code
    Функция some_func выполнялась 0.0001 сек
'''


import time


def func_time(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        res = func(*args, **kw)
        t2 = time.time()

        print('Функция {func} выполнялась {timing:2.4f} сек'.format(func=func.__name__, timing=t2-t1))

        return res
    return wrapper


@func_time
def lucky_count(from_n, to_n):
    count = 0

    for i in range(int(from_n), int(to_n)+1):
        number = list(map(int, str(i).zfill(6)))

        if sum(number[:3]) == sum(number[3:]):
            count += 1

    return count


print(lucky_count(0, 999999))
