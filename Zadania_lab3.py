import random


def zadanie_1():
    A = {1 - x for x in range(1, 11)}
    B = {4**y for y in range(8)}
    C = {z for z in B if z % 2 == 0}
    print(A)
    print(B)
    print(C)


def zadanie_2():
    lista_1 = []
    for i in range(11):
        x = random.randint(0, 100)
        lista_1.append(x)
    print(lista_1)
    lista_parzysta = [x for x in lista_1 if x % 2 == 0]
    print(lista_parzysta)


def zadanie_3():
    produkty_do_kupienia = {"ziemiaki": "kg", "chleb": "sztuki", "mleko": "litry", "mięso": "kg", "myszki": "sztuki", "karty_graficzne": "sztuki", "monitory": "sztuki"}
    tylko_sztuki = []

    for key, values in produkty_do_kupienia.items():
        if values == "sztuki":
            tylko_sztuki.append(key)
    print(tylko_sztuki)



def zadanie_4():
    lista_bokow = []
    a = int(input("Podaj bok a:"))
    lista_bokow.append(a)
    b = int(input("Podaj bok b:"))
    lista_bokow.append(b)
    c = int(input("Podaj bok c:"))
    lista_bokow.append(c)
    lista_bokow.sort()
    if lista_bokow[0] ** 2 + lista_bokow[1] ** 2 == lista_bokow[2] ** 2:
        print("Trójkąt jest prostokątny!")


def zadanie_5(a, b, h):
    pole = 0.5 * (a + b) * h
    return pole


def zadanie_6(a = 1, b = 4, ile = 10):
    x = a * b
    ciag = [x]
    for i in range(ile-1):
        y = ciag[i] * b
        ciag.append(y)
    return ciag


def zadanie_7():
    x = int(input("Podaj liczbę:"))
    if x < 0:
        return "Podanej liczby nie da się spierwiastkować"

    else:
        pierwiastek = x ** 0.5
        return pierwiastek


def main():
    zadanie_1()
    zadanie_2()
    zadanie_3()
    zadanie_4()
    print(zadanie_5(4, 6, 2))
    print(zadanie_6())
    print(zadanie_7())

if __name__=='__main__':
    main()

