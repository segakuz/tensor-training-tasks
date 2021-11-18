""""Прибавить к любой дате 1 месяц и вывести в формате ДД.ММ.ГГГГ"""


from datetime import date


def get_date_plus_month(date_obj):
    return date(date_obj.year + int(date_obj.month / 12), ((date_obj.month % 12) + 1), date_obj.day)


print(get_date_plus_month(date(2021, 12, 5)))
