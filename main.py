"""Main program module with console interface."""

from repository.car_repository import CarRepository


def read_initial_data() -> list[str]:
    """Read source records until an empty line."""
    data_list: list[str] = []

    while True:
        line = input("> ").strip()
        if not line:
            break
        data_list.append(line)

    return data_list


def print_menu() -> None:
    """Print available user commands."""
    print("\n1. Все")
    print("2. Фильтр")
    print("3. Поиск")
    print("4. Выход")


def print_cars(cars: list[object]) -> None:
    """Print cars returned by repository queries."""
    for car in cars:
        print(car)


def handle_month_filter(repo: CarRepository) -> None:
    """Ask for month filter parameters and print matching cars."""
    try:
        year = int(input("Год: "))
        month = int(input("Месяц: "))
    except ValueError:
        print("Ошибка ввода")
        return

    print_cars(repo.filter_by_month(year, month))


def handle_number_search(repo: CarRepository) -> None:
    """Ask for a number and print matching cars."""
    number = input("Номер: ")
    print_cars(repo.find_by_number(number))


def main() -> None:
    """Run the console interface."""
    data_list = read_initial_data()

    if not data_list:
        print("Нет данных")
        return

    repo = CarRepository()
    for error in repo.add_from_strings(data_list):
        print(error)

    while True:
        print_menu()
        choice = input("> ")

        if choice == "1":
            print_cars(repo.get_all())
        elif choice == "2":
            handle_month_filter(repo)
        elif choice == "3":
            handle_number_search(repo)
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
