import datetime
import re
from dateutil.relativedelta import relativedelta


class Person:

    dey_of_death = ""
    first_name = ""
    last_name = ""
    second_name = ""
    sex = ""
    age = 0
    birthday = ""

    def __init__(self, first_name, last_name, birthday, sex, second_name="", day_of_death="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = self.__convert_to_date(birthday)
        self.sex = sex
        self.second_name = second_name
        if day_of_death:
            self.dey_of_death = self.__convert_to_date(day_of_death)
        if age:
            self.age = age
        else:
            self.age = self.__calculate_age()

    def __convert_to_date(self, str_date):
        day, month, year = (int(i.strip()) for i in re.split("-|/| |\.", str_date))
        return datetime.date(day=day, month=month, year=year)

    def __calculate_age(self):
        if self.dey_of_death:
            return relativedelta(self.dey_of_death, self.birthday).years
        else:
            return relativedelta(datetime.date.today(), self.birthday).years


if __name__ == "__main__":
    I = Person("Sasha", "Boiko", "11 06 1996", "M")
    print(I.birthday)
    print(I.age)

