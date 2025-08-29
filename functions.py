import random
from settings import BASE_DIR, base, month
from openpyxl import load_workbook
import calendar
from datetime import datetime
ttn = load_workbook("import/ttnweight2.xlsx")
sheet = ttn.active
values = sheet.cell(row=16, column=30).value

def date_number_document(colum):
    data_number = colum.cell(row=39, column=8).value
    date_month = colum.cell(row=39, column=13).value
    year = colum.cell(row=39, column=28).value

    year = int(year[0:4])
    _,num_days = calendar.monthrange(year, month.values('Июнь'))

    print(num_days)

def examination_machine2(colum, row: int, column: int, basa):
    documen_namber = colum.cell(row=4, column=103).value
    documen_date = colum.cell(row=5, column=103).value
    document = f"ТТН {documen_namber} от {documen_date}"
    values = colum.cell(row=row, column=column).value
    if values == "Гайирбеков Ибрагим Расулович":
        ducument = colum.cell(row=62, column=31, value=document).value
        values = colum.cell(row=18, column=89).value
        values = colum.cell(row=26, column=105, value=values).value
        return values, ducument, True
    else:
        values = colum.cell(row=18, column=89).value
        values = colum.cell(row=26, column=105, value=values).value
        machine1 = basa["machine2"]
        machine1_driver = machine1["driver"]
        machine1_driver = colum.cell(row=49, column=6, value=machine1_driver).value
        machine1_driver = colum.cell(row=33, column=94, value=machine1_driver).value
        machine1_driver = colum.cell(row=72, column=17, value=machine1_driver).value
        machine1_driver = colum.cell(row=69, column=73, value=machine1_driver).value
        machine1_certificate = machine1['certificate']
        machine1_certificate = colum.cell(row=49, column=51, value=machine1_certificate).value
        machine1_state_signs = machine1['state_signs']
        machine1_state_signs = colum.cell(row=45, column=63, value=machine1_state_signs).value
        machine1_trailer = machine1["trailer"]
        machine1_trailer = colum.cell(row=55, column=83, value=machine1_trailer).value
        ducument = colum.cell(row=62, column=31, value=document).value

        return machine1_driver, machine1_certificate, machine1_state_signs, machine1_trailer, values, ducument


def examination_machine1(colum, row: int, column: int, basa):
    documen_namber = colum.cell(row=4, column=103).value
    documen_date = colum.cell(row=5, column=103).value
    document = f"ТТН {documen_namber} от {documen_date}"
    values = colum.cell(row=row, column=column).value
    if values == "Джанбулатов Руслан Джанболатович":
        ducument = colum.cell(row=62, column=31, value=document).value
        values = colum.cell(row=18, column=89).value
        values = colum.cell(row=26, column=105, value=values).value

        return values, ducument, True
    else:
        values = colum.cell(row=18, column=89).value
        values = colum.cell(row=26, column=105, value=values).value
        machine1 = basa["machine1"]
        machine1_driver = machine1["driver"]
        machine1_driver = colum.cell(row=49, column=6, value=machine1_driver).value
        machine1_driver = colum.cell(row=33, column=94, value=machine1_driver).value
        machine1_driver = colum.cell(row=72, column=17, value=machine1_driver).value
        machine1_driver = colum.cell(row=69, column=73, value=machine1_driver).value
        machine1_certificate = machine1['certificate']
        machine1_certificate = colum.cell(row=49, column=51, value=machine1_certificate).value
        machine1_state_signs = machine1['state_signs']
        machine1_state_signs = colum.cell(row=45, column=63, value=machine1_state_signs).value
        machine1_trailer = machine1["trailer"]
        machine1_trailer = colum.cell(row=55, column=83, value=machine1_trailer).value
        ducument = colum.cell(row=62, column=31, value=document).value
        return machine1_driver, machine1_certificate, machine1_state_signs, machine1_trailer, values, ducument


def distribute_cement(total_weight):
    machine1 = []
    machine2 = []
    remaining_weight = total_weight

    while remaining_weight > 0:
        # Определяем вес для текущего рейса (случайное число от 22.0 до 25.0 или остаток)
        if remaining_weight >= 22.0:
            # Генерируем случайный вес от 22.0 до 25.0, но не больше оставшегося
            load = round(random.uniform(22.0, min(25.0, remaining_weight)), 1)
        else:
            load = remaining_weight  # последний рейс берет остаток (может быть < 22.0)

        # Распределяем между машинами по очереди
        if len(machine1) <= len(machine2):
            machine1.append(load)
        else:
            machine2.append(load)

        remaining_weight -= load
        remaining_weight = round(remaining_weight, 1)  # округление для избежания ошибок float

    # Проверка общего веса
    sum1 = round(sum(machine1), 1)
    sum2 = round(sum(machine2), 1)
    assert abs((sum1 + sum2) - total_weight) < 0.1, f"Ошибка: общий вес не совпадает! {sum1 + sum2} != {total_weight}"

    return machine1, machine2


def ttn_save_machine1(machine1, column, file):
    count = len(machine1)
    for i, weight in enumerate(machine1, count):
        column.cell(row=21, column=84, value=weight)
        examination_machine1(sheet, 49, 6, base)

        file.save(BASE_DIR / f"export/machine1/ttnweight{i}.xlsx")


def ttn_save_machine2(machine2, column, file):
    count = len(machine2)
    for i, weight in enumerate(machine2, count):
        column.cell(row=21, column=84, value=weight)
        examination_machine2(sheet, 49, 6, base)

        file.save(BASE_DIR / f"export/machine2/ttnweight{i}.xlsx")



date_number_document(sheet)
# machine1, machine2 = distribute_cement(values)
# text_machine1 = f"Машина 1 сделала {len(machine1)} рейсов: {machine1}"
# text_machine2 = f"Машина 2 сделала {len(machine2)} рейсов: {machine2}"
# all_machine1 = f"Общий вес машины 1: {sum(machine1)}"
# all_machine2 = f"Общий вес машины 2: {sum(machine2)}"
# text = f"Проверка: общий вес = {sum(machine1) + sum(machine2)} (исходный вес: {values})"
# machine1 = ttn_save_machine1(machine1, sheet, ttn)
# machine2 = ttn_save_machine2(machine2, sheet, ttn)
