"""Получить текущую дату в формате ДД.ММ.ГГГГ"""


from datetime import date


def get_current_date():
    return date.today().strftime('%d.%m.%Y')


print(get_current_date())
