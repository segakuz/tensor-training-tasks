"""Написать функцию change_month, которая к переданной дате прибавляет/вычитает переданное
кол-во месяцев.
Например:
   change_month(’12.12.12’, 7) -> ’12.07.13’
   change_month(’01.11.10’, -5) -> ’01.06.10’"""


from datetime import datetime
import calendar


def change_month(date_str, months):
    dt = datetime.strptime(date_str, '%d.%m.%y')

    m = (dt.month + months) % 12
    if not m:
        m = 12
    y = dt.year + (dt.month + months - 1) // 12
    d = min(dt.day, calendar.monthrange(y, m)[1])

    return dt.replace(day=d, month=m, year=y).strftime('%d.%m.%y')


print(change_month('12.12.12', 7))
print(change_month('12.12.12', 12))
print(change_month('01.11.10', -5))
print(change_month('01.11.10', -11))
