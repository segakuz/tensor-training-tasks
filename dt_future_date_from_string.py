"""На входе есть строка '03.05.13' надо к этой дате прибавить 10 дней и вывести в формате
ДД.ММ.ГГГГ"""


from datetime import datetime
from datetime import timedelta


def get_future_date_from_string(date_string, days=10):
    dt = datetime.strptime(date_string, '%d.%m.%y')

    return (dt + timedelta(days=days)).strftime('%d.%m.%y')


print(get_future_date_from_string('03.05.13'))
