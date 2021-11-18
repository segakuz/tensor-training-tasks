"""Вывести дату в формате ДД.ММ.ГГ, эта дата должна быть первым днем месяца"""


from datetime import date


def get_first_day_of_month():
    return date.today().replace(day=1).strftime('%d.%m.%y')


print(get_first_day_of_month())
