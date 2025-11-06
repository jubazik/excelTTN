from pathlib import Path
import calendar


def number_check(check):  # Проверка число на четность
    if check % 2 == 0:
        print(f"число {check} - четное ")
        return 2
    else:
        print(f"число {check} - нечетное ")
        return 1


def examination_in_month_day(year, month_):  # проверка сколько дней в месяцу
    for key, value in month.items():
        if value == month_:
            return calendar.monthrange(int(year), int(key))[1]

folder_path_machine1 = "export/machine1"
folder_path_machine2 = "export/machine2"
folder = "export"
BASE_DIR = Path(__file__).parent

base = {
    "machine1": {
        "driver": "Джанбулатов Руслан Джанболатович",
        "certificate": "523 713 004",
        "car": "МАЗ 643028",
        "state_signs": "С315РН05",
        "trailer": "AM44705"

    },
    "machine2": {
        "driver": "Гайирбеков Ибрагим Расулович",
        "certificate": "99 00  166121",
        "car": "МАЗ 643028",
        "state_signs": "С337РН05",
        "trailer": "AM502305"
    }
}

month = {
    '1': 'января',
    '2': 'февраля',
    '3': 'марта',
    '4': 'апреля',
    '5': 'мая',
    '6': 'июня',
    '7': 'июля',
    '8': 'августа',
    '9': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}



month__ = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

document = ''

driver = ["R49C6", "R33C94", "R72C17", "R69C73"]
certificate = 'R49C51'
state_signs = "R45C63"
trailer = "R55C83"
machine1 = base["machine1"]

all_sum = "R18C89"
summ = "R26C105"
