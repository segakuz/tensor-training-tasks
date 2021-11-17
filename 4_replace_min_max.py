# Поменять местами самый большой и самый маленький элементы списка


def replace_min_max(numbers):
    min_n = min(numbers)
    min_i = numbers.index(min_n)
    max_n = max(numbers)
    max_i = numbers.index(max_n)

    numbers[min_i] = max_n
    numbers[max_i] = min_n

    return numbers


print(replace_min_max([10, 1, 100, 99, 666, 13]))
