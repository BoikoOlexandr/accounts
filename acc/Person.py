import datetime
import logging
import re
from dateutil.relativedelta import relativedelta


class Person:
    id = 0
    dey_of_death = ""
    first_name = ""
    last_name = ""
    second_name = ""
    sex = ""
    age = 0
    birthday = ""

    def __init__(self, id=0, first_name="", second_name="", last_name="", age=0, birthday="", day_of_death="", sex=""):
        self.first_name = first_name
        self.last_name = last_name
        if re.search("\d\d\d\d-\d\d-\d\d", birthday):
            self.birthday = birthday
        else:
            self.birthday = self.__convert_to_date(birthday)
        self.sex = sex
        self.second_name = second_name
        if day_of_death:
            self.dey_of_death = self.__convert_to_date(day_of_death)

        if age:
            self.age = age
        else:

            self.age = self.__calculate_age()
        if id:
            self.id = id

    def __convert_to_date(self, str_date):
        try:
            day, month, year = (int(i.strip()) for i in re.split("-|/| |\.|-", str_date))
            return datetime.date(day=day, month=month, year=year)
        except Exception:
            logging.warning(f"Can`'t transform '{str_date}' to valid date")
            return None

    def __calculate_age(self):
        if self.dey_of_death:
            return relativedelta(self.dey_of_death, self.birthday).years
        else:
            return relativedelta(datetime.date.today(), self.birthday).years

    def __repr__(self):
        statement = f"{self.first_name} {self.second_name} {self.last_name} {self.age} years old"
        return statement.replace("None", "")


if __name__ == "__main__":
    I = Person(first_name="Vitaliy", last_name="Serhienko", birthday="11-06-1996", sex="M")
    print(I.birthday)
    print(I.age)
