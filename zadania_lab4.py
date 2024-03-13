import math
import random


def wyrazenia():
    print("%.2f" % math.cbrt(math.e**4 - math.log2(34)))
    print("%.2f" % math.cbrt(math.log(20) + math.cos(45) + math.e))
    print("%.2f" % (math.log(20, 3) + math.sin(45) * 5/8)**0.25)
    print("%.2f" % (math.log(23, 3) + math.cbrt(math.sin(34) + 5)))
    print("%.2f" % (math.log2(32) + math.pi + math.sin(56))**0.25)


def wieza(x):
    if x <= 10:
        for _ in range(1, x+1):
            print("A" * _)


def piramida(x):
    if x <= 10:
        for _ in range(1, x+1):
            s = x - _
            if _ == 1:
                print(" " * s, "A" * _)
            elif _ == 2:
                print(" " * s, "A" * 3)
            else:
                print(" " * s, "A" * (_*2-1))


def wektor_nxn(y):
    for i in range(y):
        suma = 0
        for j in range(y):
            x = random.randint(0, 100)
            suma += x
            if j < y:
                print(f"{x} ", end=" ")
        print(f"= {suma}\n")


def main():
    wyrazenia()
    x = int(input("Podaj wysokość wieży:"))
    wieza(x)
    x = int(input("Podaj wysokość piramidy:"))
    piramida(x)
    y = int(input("Podaj wielkość wektora nxn:"))
    wektor_nxn(y)


if __name__ == '__main__':
    main()
