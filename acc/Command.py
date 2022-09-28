from acc.Person import Person
from acc.account import Account


class Command:
    command_code = 0

    def __init__(self):
        self.account = Account()
        self.commands = [
            self.add,
            self.search
        ]

    def set_command(self, command_code):
        self.commands[command_code-1]()

    def search(self):
        first_name = input("Enter first name: ")
        second_name = input("Enter second name: ")
        last_name = input("Enter last name: ")
        self.account.find_persons(first_name, second_name, last_name)

    def add(self):
        while True:
            first_name = input("Enter first_name: ")
            first_name.capitalize()
            if first_name: break

        second_name = input("Enter second_name: ")
        last_name = input("Enter last name: ")
        while True:
            birth_day = input("Enter birthday: ")
            if birth_day: break

        day_of_death = input("Enter day of death: ")
        while True:
            sex = input("Enter sex(M/F): ")
            sex = sex.upper()
            if sex in ['M', 'F']:
                break
        self.account.add_person(
            Person(first_name=first_name, second_name=second_name, last_name=last_name, birthday=birth_day,
                   day_of_death=day_of_death, sex=sex)
        )
