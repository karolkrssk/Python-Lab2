class Dziennik:
    def __init__(self, student_list):
        if student_list is None:
            self.__student_list = []
        else:
            self.__student_list = student_list

    @property
    def student_list(self):
        return self.__student_list

    @student_list.setter
    def student_list(self, value):
        self.__student_list = value

    @staticmethod
    def weighted_avg(values, weights):
        if len(values) != 0 and len(weights) != 0:
            s = 0
            for x, y in zip(values, weights):
                s += x * y

            average = s / sum(weights)
            return average
        else: print("Najpierw Uzupełnij wagi i oceny")

    def show_grades(self, ID=0):
        print(50 * "-")
        print(f"Szukam ucznia o ID: {ID} \nJeżeli nie ma ucznia o zadanym ID nic się nie wyświetli")
        print(50 * "-")
        try:

            for el in self.student_list:
                if el.ID == ID:
                    print(f"ID: {el.ID}")
                    print(f"Imię: {el.name}")
                    print(f"Nazwisko: {el.lastname}")
                    if len(el.grades) != 0:
                        print(f"Oceny: {el.grades}")
                        print(f"Wagi : {el.rate}")
                    else:
                        print("Uczeń nie ma ocen")
        except:
            print("Wprowadź poprwaną wartość!")
   


    def print_all(self):
        for el in self.student_list:
            print(50 * "-")
            print(f"ID: {el.ID}")
            print(f"Imię: {el.name}")
            print(f"Nazwisko: {el.lastname}")
            if len(el.grades) != 0:
                print(f"Oceny: {el.grades}")
                print(f"Waga : {el.rate}")
                print(f"Średnia ocen: {self.weighted_avg(el.grades, el.rate)}")
            else:
                print("Uczeń nie ma ocen")