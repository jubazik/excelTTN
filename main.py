# from functions import TTNApp
# import tkinter as tk
#
#
# def main():
#     root = tk.Tk()
#     app = TTNApp(root)
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()
from functions import get_weight_from_file, distribute_cement

if __name__ == "__main__":
    # Пример использования в консольном режиме
    import sys

    if len(sys.argv) > 1:
        # Если передан аргумент - путь к файлу
        filepath = sys.argv[1]
        try:
            values = get_weight_from_file(filepath)
            print(f"Вес из файла: {values}")

            machine1, machine2 = distribute_cement(values)
            text_machine1 = f"Машина 1 сделала {len(machine1)} рейсов: {machine1}"
            text_machine2 = f"Машина 2 сделала {len(machine2)} рейсов: {machine2}"
            all_machine1 = f"Общий вес машины 1: {sum(machine1)}"
            all_machine2 = f"Общий вес машины 2: {sum(machine2)}"
            text = f"Проверка: общий вес = {sum(machine1) + sum(machine2)} (исходный вес: {values})"

            print(text_machine1)
            print(text_machine2)
            print(all_machine1)
            print(all_machine2)
            print(text)

        except Exception as e:
            print(f"Ошибка: {str(e)}")
    else:
        print("Использование: python main.py <путь_к_файлу_ttn>")
        print("Или запустите gui.py для графического интерфейса")
# Пример использования


