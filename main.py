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
    with open("data.txt", "r") as f:
        data = f.readlines()
    CarList = MakeCarList(data)
    CarList.print_car_list()
    print("\n")
    CarList.sort_car_by_month("1000", "01")
    print("\n")
    CarList.print_car_by_number("G044NT124")