import time

def parzysta():
    liczba = int(input("Wpisz liczbę: "))
    if liczba % 2 == 0:
        print("Liczba parzysta")
    else:
        print(f"Liczba nieparzysta. Reszta: {liczba % 2}")


def dodatnia():
    liczba = int(input("Wpisz liczbę: "))
    if liczba > 0:
        print("Dodatnia")
    elif liczba == 0:
        print("0")
    else:
        print("Ujemna")


def dodatnia2(wartosc: int):
    if wartosc > 0:
        print("Dodatnia")
    elif wartosc == 0:
        print("0")
    else:
        print("Ujemna")


def anim():
    klatka = ["  o\n/[]\ \n ||","  o\n/[]\ \n |\ ","   o\n /[]\ \n  ||","  o\n /[]\ \n  ||","  o\n /[]\ \n  /|"," o\n/[]\ \n ||"]
    for i in range(len(klatka)):
        print("\n\n\n\n\n\n" + klatka[i])
        time.sleep(0.5)
    anim()


# MAIN ####################################################

def main():
    # parzysta()
    # dodatnia()
    # dodatnia2(int(input("Dej liczbe: ")))
    anim()
    pass


if __name__ == "__main__":
    main()

