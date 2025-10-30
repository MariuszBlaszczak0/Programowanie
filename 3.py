# ZADANIA #################################################################################################


from random import randint


def zadanie1():
    for i in range(50):
        print(randint(3, 6), end=" ")
    print("")


def zadanie2():
    x = randint(1, 50)
    y = randint(2, 5)
    print(x ** y)


def zadanie3():
    ver = input("Wersja 1? t/n: ")
    if ver == "t":
        print("Mariusz" * randint(1, 10))
    else:
        for i in range(randint(1, 10)):
            print("Mariusz", end=" ")
        print("")


def zadanie4():
    for i in range(1, 51):
        print(randint(1, i+1), end=" ")
    print("")


def zadanie5():
    for i in range(8, 90, 3):
        print(i, end=" ")
    print("")


def zadanie6():

    x = input("Podaj Imię: ")
    y = int(input("Podaj ilość razy: "))
    ver = input("Wersja 1? t/n: ")
    if ver == "t":
        print(x * y)
    else:
        for i in range(y):
            print(x)


def zadanie7():
    ver = input("Wersja 1? t/n: ")
    if ver == "t":
        for i in range(20):
            print(1 + i, (1 + i) ** 2, sep=":", end=" ")
    else:
        lista = ""
        for i in range(20):
            lista = lista + str(1+i) + ":" + str((1+i)**2) + " "
        print(lista)


# DZIAŁANIA ##########################################################################################


def dodawanie(a, b):
    print(f"a + b = {a+b}")


def odejmowanie(a, b):
    print(f"a - b = {a - b}")


def mnozenie(a, b):
    print(f"a * b = {a * b}")


def dzielenie(a, b):
    print(f"a / b = {a / b}")


def dziel_cal(a, b):
    print(f"a // b = {a // b}")


def reszta(a, b):
    print(f"a % b = {a % b}")


def potega(a, b):
    print(f"a ** b = {a ** b}")


def dzialania():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    dodawanie(a, b)
    odejmowanie(a, b)
    mnozenie(a, b)
    dzielenie(a, b)
    dziel_cal(a, b)
    reszta(a, b)
    potega(a, b)

# MAIN ######################################################################################################


def main():
    pass
    #zadanie1()
    #zadanie2()
    #zadanie3()
    #zadanie4()
    #zadanie5()
    #zadanie6()
    #zadanie7()


if __name__ == "__main__":
    main()
