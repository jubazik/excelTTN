import datetime
from pathlib import Path
from traceback import print_tb
import calendar
folder = "export"
BASE_DIR = Path(__file__).parent

base ={
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
    '01' : 'Январь',
    '02' : 'Февраль',
    '03' : 'Март',
    '04' : 'Апрель',
    '05' : 'Май',
    '06' : 'Июнь',
    '07' : 'Июль',
    '08' : 'Август',
    '09' : 'Сентябрь',
    '10' : 'Октябрь',
    '11' : 'Ноябрь',
    '12' : 'декабря'
}


document = ''

driver = "R49C6", "R33C94", "R72C17", "R69C73"
certificate = 'R49C51'
state_signs = "R45C63"
trailer = "R55C83"
machine1 = base["machine1"]


print(machine1['driver'],
      machine1['certificate'])
all_sum = "R18C89"
summ = "R26C105"



"""
нужно проверить сколько дней в месяце 
в день могут делать только три рейса каждая машина 

задание 
нужно проверить сколько дней в месяце 
распределить рейсы машин по дням ( в день максимум 3 рейса )

"""