""""Прибавить к любой дате 1 месяц и вывести в формате ДД.ММ.ГГГГ"""


from training_tasks.dt_change_month import change_month


if __name__ == "__main__":
    print(change_month('11.12.87', 1, '%d.%m.%Y'))
