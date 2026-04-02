from repository.car_repository import CarRepository


def main():
    data_list = []

    while True:
        line = input("> ").strip()
        if not line:
            break
        data_list.append(line)

    if not data_list:
        print("Нет данных")
        return

    repo = CarRepository()
    repo.add_from_strings(data_list)

    while True:
        print("\n1. Все")
        print("2. Фильтр")
        print("3. Поиск")
        print("4. Выход")

        choice = input("> ")

        if choice == "1":
            for car in repo.get_all():
                print(car)

        elif choice == "2":
            try:
                year = int(input("Год: "))
                month = int(input("Месяц: "))
                for car in repo.filter_by_month(year, month):
                    print(car)
            except ValueError:
                print("Ошибка ввода")

        elif choice == "3":
            number = input("Номер: ")
            for car in repo.find_by_number(number):
                print(car)

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
