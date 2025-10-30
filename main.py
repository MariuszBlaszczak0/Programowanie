import random


def podwojna_suma(n):
    suma = 0
    for i in range(n):
        liczba = float(input("Podaj liczbę rzeczywistą: "))
        if liczba > 0:
            suma = suma + (2 * liczba)
    print(suma)


def zlicz_znaki(n):
    dodatnie = 0
    ujemne = 0
    zero = 0
    for i in range(n):
        liczba = float(input("Podaj liczbę rzeczywistą: "))
        if liczba > 0:
            dodatnie = dodatnie + 1
        elif liczba < 0:
           ujemne = ujemne + 1
        else:
            zero = zero + 1
    print(f"Dodatnie: {dodatnie}, Zero:{zero}, Ujemne:{ujemne}")


def min_max(n):
    najmniejsza = 0
    najwieksza = 0
    for i in range(n):
        liczba = float(input("Podaj liczbę rzeczywistą: "))
        if liczba > najwieksza:
            najwieksza = liczba
        elif liczba < najmniejsza:
            najmniejsza = liczba
    print(f"Najmniejsza:{najmniejsza}, Największa:{najwieksza}")


def c_do_f(c):
    f = ((9 / 5) * c) + 32
    return f


def f_do_c(f):
    c = (f - 32) * (5 / 9)
    return c


def c_czy_f(t, n):
    wynik = 0
    if n == "c":
        wynik = c_do_f(t)
    elif n == "f":
        wynik = f_do_c(t)
    return wynik


def zgadnij_liczbe():
    liczba = random.randrange(1, 11)
    print(liczba)
    proby = 5
    for i in range(proby):
        print(f"Próba: {i+1}")
        traf = int(input("Zgadnij: "))
        if traf == liczba:
            print("Trafiłeś!")
            break
        elif i == (proby - 1):
            print("Przegrałeś!")
            return


def kpn():
    pG = 0
    pK = 0
    wG = 0
    wK = 0
    for i in range(5):
        wK = random.randint(1, 3)
        if wK == 1:
            wK = "k"
        elif wK == 2:
            wK = "p"
        else:
            wK = "n"
        wG = str(input("k/p/n: "))
        if (wG == "k" and wK == "n") or (wG == "p" and wK == "k") or (wG == "n" and wK == "p"):
            pG = pG + 1
            print(f"Gracz: {wG}, Komputer: {wK} | Punkt dla gracza")
        elif wG == wK:
            print(f"Gracz: {wG}, Komputer: {wK} | Brak punktów.")
        else:
            pK = pK + 1
            print(f"Gracz: {wG}, Komputer: {wK} | Punkt dla komputera.")
    print(f"Gracz: {pG}, Komputer: {pK}")
    if pG > pK:
        print("Wygrałeś")
    elif pG == pK:
        print("Remis")
    else:
        print("Przegrałeś")


def kpn2():
    remis = 0
    pG = 0
    pK = 0
    wG = ["Kamień", "Papier", "Nożyce"]
    wK = ["Kamień", "Papier", "Nożyce"]
    for i in range(5):
        komputer = random.randint(0, 2)
        gracz = ((int(input("----------\nKAMIEŃ - 1 \nPAPIER - 2 \nNOŻYCE - 3 \n----------\nPodaj wybór: "))) - 1)
        if (wG[gracz] == wG[0] and wK[komputer] == wK[2]) or (wG[gracz] == wG[1] and wK[komputer] == wK[0]) or (wG[gracz] == wG[2] and wK[komputer] == wK[1]):
            pG = pG + 1
            print(f"----------\nGracz: {wG[gracz]}, Komputer: {wK[komputer]} | Punkt dla gracza")
        elif wG[gracz] == wK[komputer]:
            print(f"----------\nGracz: {wG[gracz]}, Komputer: {wK[komputer]} | Brak punktów.")
            remis = remis + 1
        else:
            pK = pK + 1
            print(f"----------\nGracz: {wG[gracz]}, Komputer: {wK[komputer]} | Punkt dla komputera.")
    print(f"----------\nGracz: {pG}, Komputer: {pK}, Remis: {remis}\n----------")
    if pG > pK:
        print("Wygrałeś\n----------")
    elif pG == pK:
        print("Remis\n----------")
    else:
        print("Przegrałeś\n----------")


# MAIN ################################################################


def main():
    # podwojna_suma(int(input("Podaj ilość powtórzeń: ")))

    # zlicz_znaki(int(input("Podaj ilość powtórzeń: ")))

    # min_max(int(input("Podaj ilość powtórzeń: ")))

    # temperatura = c_czy_f(float(input("Podaj temperaturę: ")), str(input("Podaj jednostkę (c/f): ")))
    # print(temperatura)

    # zgadnij_liczbe()

    kpn2()

    pass


if __name__ == "__main__":
    main()
