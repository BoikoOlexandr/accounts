import logging
import sqlite3


class DbProcessing:
    connection = None
    table = "Persons"
    sql = ""

    def __init__(self):
        self.connection = sqlite3.connect('person.db')
        self.cursor = self.connection.cursor()

    def add(self, **data):
        columns = "("
        values = "("
        for key, value in data.items():
            columns += key + ","
            values += f"'{str(value)}',"
        columns = columns[:-1] + ")"
        values = values[:-1] + ")"
        self.sql = f"INSERT INTO {self.table}{columns} VALUES {values}"
        self.__execute()

    def search(self, first_name="", second_name="", last_name=""):
        and_statement = " AND "
        statements = []
        if first_name:
            statements.append(f"first_name LIKE '{first_name}%'")
        if second_name:
            statements.append(f"first_name LIKE '{first_name}%'")
        if last_name:
            statements.append(f"first_name LIKE '{first_name}%'")
        self.sql = "SELECT 	* FROM 	Persons WHERE "
        for statement in statements:
            self.sql += statement + and_statement
        self.sql = self.sql[:-and_statement.__len__()]
        return self.__fetch()

    def __fetch(self):
        try:
            self.cursor.execute(self.sql)
            return self.cursor.fetchall()
        except sqlite3.OperationalError as e:
            logging.warning(f"cant fetch from Sql statement \n'{ self.sql}' \nget error {e}")
            return None

    def __execute(self):
        try:
            self.cursor.execute( self.sql)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            logging.warning(f"Can't execute Sql statement \n'{ self.sql}' \nget error {e}")


if __name__ == "__main__":
    a = DbProcessing()
    print(a.search(first_name="Sa"))
