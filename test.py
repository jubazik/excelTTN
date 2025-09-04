import datetime
import calendar

month = {
    '1': 'Января',
    '2': 'Февраля',
    '3': 'Марта',
    '4': 'Апреля',
    '5': 'Мая',
    '6': 'Июня',
    '7': 'Июля',
    '8': 'Августа',
    '9': 'Сентября',
    '10': 'Октября',
    '11': 'Ноября',
    '12': 'Декабря'
}

def examination_in_month_day(year, month_):  # проверка сколько дней в месяцу
    for key, value in month.items():
        if value == month_:
            return calendar.monthrange(int(year), int(key))[1]

def switching_days_and_months(data_number, data_month):
    year = 2025
    new_data = 0
    count = 3
    while count != 0:
        pass



count = 3
while count != 0:
    print('3')
    count -= 1
switching_days_and_months(12, 12)