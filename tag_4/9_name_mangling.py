"""
Name Mangling: Mechanismus, um in vererbten Klassen zu verhindern, dass
Methoden von Basis-Klassen aufgerufen werden.
"""


class Database:
    def __init__(self):
        self.__host = "localhost"  # _Database__host
        self.__load()  # private
        self.connect()  # public

    def __load(self):
        print("loading Database ...")

    def connect(self):
        print("connect Database")


class Controller(Database):
    def __load(self):
        print("loading Controller")

    def connect(self):
        print("connect Controller")
        # print(self.__host)


d = Controller()  # es wird das __load von Database
# print(dir(d))
print(dir(d))
