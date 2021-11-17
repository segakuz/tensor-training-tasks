'''Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов.
Билеты начинаются с 000000 и заканчиваются 999999. Счастливым считается билет, если сумма
первых трех значений, равна сумме вторых трёх (Например: 927864, 123006, 002110 и т.д.)'''


def lucky_count(from_n, to_n):
    count = 0

    for i in range(int(from_n), int(to_n)+1):
        number = list(map(int, str(i).zfill(6)))

        if sum(number[:3]) == sum(number[3:]):
            count += 1

    return count


print(lucky_count('000000', '999999'))
# print(lucky_count(0, 999999))
