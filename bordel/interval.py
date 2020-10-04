#!/usr/bin/python

pole = []
i = int(-1)


def normal():
    global i, interval, pole
    i = i + 1
    interval = interval + 1
    pole.append(interval)


def sude():  # sudé se používá i na liché
    global i, interval, pole
    i = i + 1
    interval = interval + 2
    pole.append(interval)
    

while True:
    try:
        A = int(input("Zadej první číslo: "))
        B = int(input("Zadej druhé číslo: "))
        break
    except:
        print("Byla zadaná chybná hodnota.")
        continue
if A > B:  # zde se proměnné ukládají do vedlejších proměnných a prohazují se
    Aa, Bb = int(A), int(B)
    C = int(A)
    A = B
    B = C

sudeA = int(A % 2)  # kvůli sudému a lichému
sudeB = int(B % 2)

while True:
    typ = input(
        'Zadej:\n'
        'nic pro normální\n'
        '"l" pro liché\n'
        '"s" pro sudé: ')
    if typ == "":
        interval = A - 1
        while interval != B:
            normal()
        break
    elif typ == "s":
        if sudeA == 1:
            A = A + 1
        if sudeB == 1:
            B = B - 1
        interval = A - 2
        while interval != B:
            sude()
        break
    elif typ == "l":
        if sudeA == 0:
            A = A + 1
        if sudeB == 0:
            B = B - 1
        interval = A - 2
        while interval != B:
            sude()
        break
    else:
        print("Zkus to znovu.")
        continue
try:
    if Aa > Bb:
        pole.reverse()  # zde se pole obrátí pokud B bylo větší
except:
    None
print(pole)
