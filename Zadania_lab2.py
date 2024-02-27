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
for _ in range(1, liczba):
    if liczba / _:
        dziel += 1
    if dziel == 2:
        print("Jest to liczba pierwsza")
    else:
        print("Nie jest to liczba pierwsza")


# Zadanie 5
ile_liczb = 0
for i in range(1001):
    suma = 0
    for j in range(1, i-1):
        if i / j:
            suma += j
        if i == suma:
            ile_liczb += 1
print(f"Tyle liczb doskonałych {ile_liczb}")









