"""Вывести дату в формате ДД.ММ.ГГ, эта дата должна быть последним днем месяца"""


from datetime import date
from datetime import timedelta


def get_last_month_date():
    today = date.today()

    return (today.replace(month=today.month+1, day=1) - timedelta(days=1)).strftime('%d.%m.%y')


print(get_last_month_date())
