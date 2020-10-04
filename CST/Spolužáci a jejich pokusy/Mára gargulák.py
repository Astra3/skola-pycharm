from DCBLP import *
from wiringpi2 import *
from time import *


def prevod(hodnota):
    return int(hodnota) * 1023


def halfadder(x, y):
    cy = x and y
    suma = x or y
    if cy == 1:
        suma = 0
    return cy, suma


def scitacka(Y3, Y2, Y1, Y0):
    cy1, Y0 = halfadder(1, Y0)
    cy2, Y1 = halfadder(cy1, Y1)
    cy3, Y2 = halfadder(cy2, Y2)
    cy4, Y3 = halfadder(cy3, Y3)
    return Y3, Y2, Y1, Y0


def dekoder(cy, sum2, sum1, sum0):
    a1 = soucet(1, 1, sum1, not sum0)
    a2 = soucet(not cy, 1, sum1, 1)
    a3 = soucet(cy, sum2, sum1, sum0)
    a4 = soucet(not cy, sum2, 1, sum0)
    a5 = soucet(cy, not sum2, not sum1, 1)
    a6 = soucet(cy, 1, not sum1, not sum0)
    a7 = soucet(not cy, not sum2, not sum1, not sum0)

    a = a1 or a2 or a3 or a4 or a5 or a6 or a7

    b1 = soucet(1, not sum2, sum1, not sum0)
    b2 = soucet(not cy, not sum2, 1, 1)
    b3 = soucet(not cy, 1, sum1, sum0)
    b4 = soucet(not cy, 1, not sum1, not sum0)
    b5 = soucet(cy, 1, not sum1, sum0)
    b6 = soucet(cy, not sum2, not sum1, 1)

    b = b1 or b2 or b3 or b4 or b5 or b6

    c1 = soucet(cy, not sum2, 1, 1)
    c2 = soucet(not cy, sum2, 1, 1)
    c3 = soucet(not cy, 1, 1, sum0)
    c4 = soucet(1, 1, not sum1, sum0)
    c5 = soucet(1, not sum2, not sum1, not sum0)

    c = c1 or c2 or c3 or c4 or c5

    d1 = soucet(1, sum2, sum1, not sum0)
    d2 = soucet(not cy, not sum2, sum1, 1)
    d3 = soucet(1, not sum2, sum1, sum0)
    d4 = soucet(1, sum2, not sum1, sum0)
    d5 = soucet(cy, sum2, not sum1, 1)
    d6 = soucet(1, not sum2, not sum1, not sum0)

    d = d1 or d2 or d3 or d4 or d5 or d6

    e1 = soucet(1, 1, sum1, not sum0)
    e2 = soucet(cy, not sum2, sum1, 1)
    e3 = soucet(not cy, not sum2, 1, not sum0)
    e4 = soucet(cy, sum2, not sum1, 1)
    e5 = soucet(cy, 1, not sum1, not sum0)

    e = e1 or e2 or e3 or e4 or e5

    f1 = soucet(1, sum2, sum1, not sum0)
    f2 = soucet(cy, not sum2, 1, 1)
    f3 = soucet(not cy, sum2, not sum1, 1)
    f4 = soucet(1, 1, not sum1, not sum0)

    f = f1 or f2 or f3 or f4

    g1 = soucet(1, 1, sum1, not sum0)
    g2 = soucet(cy, not sum2, 1, 1)
    g3 = soucet(not cy, not sum2, sum1, 1)
    g4 = soucet(cy, 1, 1, sum0)
    g5 = soucet(not cy, sum2, not sum1, 1)

    g = g1 or g2 or g3 or g4 or g5

    return a, b, c, d, e, f, g


# tady budou instance (bud instance tridy citace nebo nekolika T)

# tady jsou hotove definice vstupu a vystupu
pinMode(8, IN)  # tlacitko
pinMode(0, OUT)  # segment a
pinMode(1, OUT)  # segment b
pinMode(2, OUT)  # segment c
pinMode(3, OUT)  # segment d
pinMode(4, OUT)  # segment e
pinMode(5, OUT)  # segment f
pinMode(6, OUT)  # segment g
pinMode(9, OUT)  # pripojeni k dalsimu MCU (posilani signalu do dalsiho MCU)


def main():
    print("Running...")
    reset = 1
    Y0 = False
    Y1 = False
    Y2 = False
    Y3 = False
    while True:
        # tady bude volani metody citace nebo metod nekolika T
        c = digitalRead(8)
        Y3, Y2, Y1, Y0 = scitacka(Y3, Y2, Y1, Y0)
        reset = 0
        reset = not (Y3) and not (Y2) and not (Y1) and not (Y0)

        cislo = dekoder(Y3, Y2, Y1, Y0)
        digitalWrite(0, prevod(cislo[0]))
        digitalWrite(1, prevod(cislo[1]))
        digitalWrite(2, prevod(cislo[2]))
        digitalWrite(3, prevod(cislo[3]))
        digitalWrite(4, prevod(cislo[4]))
        digitalWrite(5, prevod(cislo[5]))
        digitalWrite(6, prevod(cislo[6]))
        digitalWrite(9, reset)
        delay(1)


if __name__ == "__main__":
    main()

