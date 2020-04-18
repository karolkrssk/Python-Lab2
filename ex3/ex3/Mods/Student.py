from random import randrange


class Student:
    students_list = []

    def __init__(self, name, lastname, oceny=None, waga=None):
        self.__name = name
        self.__lastname = lastname
        if oceny is None:
            self.__oceny = []
        else:
            self.__oceny = oceny
        if waga is None:
            self.__waga = []
        else:
            self.__waga = waga

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, value):
        self.__ID = value

    @property
    def grades(self):
        return self.__oceny

    @grades.setter
    def grades(self, value):
        self.__oceny = value

    @property
    def rate(self):
        return self.__waga

    @rate.setter
    def rate(self, value):
        self.__waga = value

    def __str__(self):
        return f"ID:{self.__ID} : Imię: {self.name} \n Oceny: {self.__oceny}"

    def add_student(self):
        print(50 * "-")
        self.students_list.append(self)
        print("Dodaję studenta...")
        self.ID = randrange(100000000, 999999999)
        print(self)
