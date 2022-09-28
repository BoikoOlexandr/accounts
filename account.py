from DbProcessing import DbProcessing
from Person import Person


class Account:

    def __init__(self):
        self.Db = DbProcessing()

    def add_person(self, person:Person):
        person_dict = {}
        for key, value in person.__dict__.items():
            if value:
                person_dict[key] = value
        self.Db.add(**person_dict)

    def find_persons(self, first_name="", second_name="", last_name=""):
        persons = self.Db.search(first_name, second_name, last_name)


if __name__ == "__main__":
    a = Account()
    a.add_person(Person("Vitaliy", "Serhienko", "11-06-1996", "M"))