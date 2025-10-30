def hello_world():
    print("Hello, World!")


def zmienne1():
    zmienna1 = 2
    zmienna2 = 3
    print(f"{zmienna1} + {zmienna2} = {zmienna1 + zmienna2}")


def zmienne2():
    zmienna1 = int(input("Wprowadź zmienną 1: "))
    zmienna2 = int(input("Wprowadź zmienną 2: "))
    print(f"{zmienna1} + {zmienna2} = {zmienna1 + zmienna2}")


def typ_zmiennej():
    x = 2
    print(f"{x}: {type(x)}")
    x = 2.1
    print(f"{x}: {type(x)}")
    x = "tekst"
    print(f"{x}: {type(x)}")
    x = 2 + 3j
    print(f"{x}: {type(x)}")
    x = True
    print(f"{x}: {type(x)}")


def user():
    user_data: str = input("Wprowadź dane: ")
    print(f"Dane od użytkownika: '{user_data}'")


def tekst():
    user_data: str = input("Wprowadź dane: ")
    print(user_data, user_data)
    print(user_data, user_data, sep="-")
    print(user_data, user_data)
    print(14)
    print(user_data, user_data, end="0")
    print(14)


def zadanie1():
    tekst1: str = input("Wprowadź tekst nr 1: ")
    tekst2: str = input("Wprowadź tekst nr 2: ")
    print(tekst1, tekst2, sep=", ")


def zadanie2():
    liczba1 = float(input("Wprowadź liczbę 1: "))
    liczba2 = float(input("Wprowadź liczbę 2: "))
    print(f"{liczba1} + {liczba2} = {liczba1 + liczba2}")


# MAIN -----------------------------------------------------------------------------------------------------------------


def main():
    # hello_world()
    # zmienne1()
    # zmienne2()
    # typ_zmiennej()
    # user()
    # tekst()
    # zadanie1()
    zadanie2()


if __name__ == "__main__":
    main()
