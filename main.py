from datetime import date
import re
class Car:
    def __init__(self, data):
        self.number = re.findall(r'"(.*?)"', data)[0]
        self.date = re.findall(r'\d{4}.\d{2}.\d{2}', data)[0]
    def __str__(self):
        return f'{self.number}  {self.date} '

class MakeCarList:
    def __init__(self, data_list):
        car_list = []
        for data in data_list:
            car_list.append(Car(data))
        self.car_list = car_list
    def sort_car_by_month(self, year, month):

        new_car_list = []
        car_list = self.car_list
        for item in car_list:
            date_args = item.date.split('.')
            if date_args[0] == year and date_args[1] == month:
                new_car_list.append(item)
            sorted_items = sorted(new_car_list, key=lambda i:i.date)

        for i in sorted_items: print(i)

    def print_car_by_number(self, number):
        for item in self.car_list:
            if item.number == number:
                print(item)
    def print_car_list(self):
        for item in self.car_list:
            print(item)


if __name__ == '__main__':
    print("Введите данные об автомобилях в формате: \"номер\" ГГГГ.ММ.ДД")
    print("Для завершения ввода оставьте строку пустой и нажмите Enter.\n")

    data_list = []
    while True:
        line = input("> ").strip()
        if line == "":
            break
        data_list.append(line)

    if not data_list:
        print("Нет данных для работы. Программа завершена.")
        exit()

    car_list = MakeCarList(data_list)
    car_list.print_car_list()


    while True:
        print("\n" + "=" * 40)
        print("Выберите действие:")
        print("1. Вывести весь список автомобилей")
        print("2. Отфильтровать автомобили по году и месяцу")
        print("3. Найти автомобиль по номеру")
        print("4. Выход")
        choice = input("Ваш выбор (1-4): ").strip()

        if choice == "1":
            print("\nСписок всех автомобилей:")
            car_list.print_car_list()

        elif choice == "2":
            year = input("Введите год (например, 2023): ").strip()
            month = input("Введите месяц (двузначное число, например, 01): ").strip()
            print(f"\nАвтомобили за {year}.{month}:")
            car_list.sort_car_by_month(year, month)

        elif choice == "3":
            number = input("Введите номер автомобиля (например, G044NT124): ").strip()
            print(f"\nАвтомобиль с номером {number}:")
            car_list.print_car_by_number(number)

        elif choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")

