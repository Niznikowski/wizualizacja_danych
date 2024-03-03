# Zadanie 1
zdanie = input("Napisz zdanie:")
x = zdanie.split()
print(len(x))


# Zadanie 2
import sys
sys.stdout.write("Wprowadź liczbę: ")
a = sys.stdin.readline()
a = int(a)
sys.stdout.write("Wprowadź liczbę: ")
b = sys.stdin.readline()
b = int(b)
sys.stdout.write("Wprowadź liczbę: ")
c = sys.stdin.readline()
c = int(c)

wynik = a ** b + c
print(wynik)


# Zadanie 3
napis = input("Wpisz napis:")
if napis == napis[::-1]:
    print("Napis jest palindromem")
else:
    print("Nie jest palindromem")


# Zadanie 4
liczba = int(input("wpisz liczbę:"))
dziel = 0
for _ in range(1, liczba+1):
    if liczba % _ == 0:
        dziel += 1
if dziel == 2:
    print("Jest to liczba pierwsza")
else:
    print("Nie jest to liczba pierwsza")


# Zadanie 5
ile_liczb = 0
for i in range(1, 1001):
    suma = 0
    for j in range(1, i-1):
        if i % j == 0:
            suma += j
    if i == suma:
        ile_liczb += 1
print(f"Tyle liczb doskonałych {ile_liczb}")


# Zadanie 6
import random
lista = []
for i in range(1, 10):
    x = int(random.randint(1, 100))
    y = float(random.randint(1, 100))
    lista.append(x)
    lista.append(y)

for j in range(len(lista)):
    lista[j] = lista[j] ** 2


# Zadanie 7
lista_7 = []
liczba = 0
while liczba < 10:
    a = int(input("Podaj liczbę:"))
    liczba += 1
    if a % 2 == 0:
        lista_7.append(a)
print(f"Lista liczby parzyste: {lista_7}")

# Zadanie 8
lista_8 = [35, "Kapusta", 90, 345, "Luk", 90, 23, "rower", '23', "rower", 23, 'Order-66', "kolejny element"]
slownik_8 = {}
for _ in lista_8:
    a = slownik_8.values()
    if _ in slownik_8.keys():
        slownik_8[_] += 1
    else:
        a = 1
        slownik_8.update({_: a})
print(f"Utworzony słownik: {slownik_8}")
tylko_cyfry = [klucz for klucz in slownik_8 if not isinstance(klucz, (int, float))]
for key in tylko_cyfry:
    del slownik_8[key]
print(f"Słownik po usunięciu elemnetów nie będących liczbami: {slownik_8}")


