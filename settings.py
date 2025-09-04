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
    '1' : 'января',
    '2' : 'февраля',
    '3' : 'марта',
    '4' : 'апреля',
    '5' : 'мая',
    '6' : 'июня',
    '7' : 'июля',
    '8' : 'августа',
    '9' : 'сентября',
    '10' : 'октября',
    '11' : 'ноября',
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



