from Mods.Student import Student
from Mods.Dziennik import Dziennik

def main():
    # Tworzenie studentów
    student1 = Student("Karol", "Krasuski")
    student1.add_student()

    student2 = Student("Piotr", "Kowalski")
    student2.add_student()

    student3 = Student("Adam", "Nowak")
    student3.add_student()

    # Dodanie ocen i wag do ocen
    student1.grades = [2, 2, 2, 2, 2]
    student1.rate = [1, 1, 1, 1, 1]
    student2.grades.append(2)
    student2.rate.append(3)

    # Tworzenie nowego dziennika w oparciu o listę studentów
    dziennik1 = Dziennik(Student.students_list)

    driver_code(dziennik1)


def driver_code(dziennik):
    try:

        choice = int(input(f"""{80 * "*"}
Wybierz którą funkcje chcesz uruchomić
Wpisz odpowiadająca poleceniu cyfrę:
{80 * "-"}
1 -> Wyświetl oceny ucznia o zadanym ID
2 -> Wyświetl dane wszystkich uczniów
0 -> Wyjście z programu
{80 * "-"}
Twój wybór: """))

        if choice == 1:
            x = int(input("Wpisz ID studenta: "))
            dziennik.show_grades(x)
            driver_code(dziennik)
        elif choice == 2:
            dziennik.print_all()
            driver_code(dziennik)
        elif choice == 0:
            print("Zamykam program...")
            exit()
        else:
            print(
                "Niepoprawna wartość! \nSpróbuj jeszcze raz lub wpisz 0 aby wyjść z programu")
            driver_code(dziennik)
    except ValueError:
        print(
            "Niepoprawna wartość! \nSpróbuj jeszcze raz lub wpisz 0 aby wyjść z programu")
        driver_code(dziennik)


if __name__ == '__main__':
    main()
