"""Получить текущую дату +5 дней в формате ДД.ММ.ГГ"""


from datetime import date
from datetime import timedelta


def get_future_date(days):
    return (date.today() + timedelta(days=days)).strftime('%d.%m.%y')


print(get_future_date(5))
