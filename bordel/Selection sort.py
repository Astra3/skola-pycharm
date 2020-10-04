#!usr/bin/python

while True:
    cisla = input("Zadejte čísla oddělená mezerami, pro desetiny použijte tečky: ")
    cisla2 = cisla.replace(" ", "")
    cisla2 = cisla2.replace(".", "")
    cisla2 = cisla2.replace("-", "")
    if cisla2.isnumeric():  # kontrola zda jsou hodnoty číselné
        break
    else:
        print("Čísla byly zadány špatně.\n"
              "Příklad: máme čísla 3, 8.2, 10.6 a 6\n"
              "Zadáme: 3 8.2 10.6 6\n")
        continue
pole = cisla.split()  # je třeba převést každou položku v poli ze str na float
for i in range(len(pole)):
    pole[i] = float(pole[i])


p = 0
while p != len(pole):
    c = -7e+1000  # Zde leží jediný limit programu, bude fungovat špatně s čísly menší jak toto
    for i in range(p, len(pole)):
        if pole[i] > c:
            i2 = i  # Uloží pozici největšího čísla
            c = pole[i]  # Uloží největší číslo kdyby se nalezlo větší
    c2 = pole[p]  # Prohození největší a první hodnoty
    pole[p] = c
    pole[i2] = c2
    p = p + 1  # Posune začátek pole

pole2 = str(pole)  # Tato část pouze upravuje pole převodem do stringu aby bylo lépe čitelné
pole2 = pole2.replace("[", "")
pole2 = pole2.replace("]", "")
pole2 = pole2.replace(", ", " >= ")  # >= proto, že někdy se stane, že jsou zadána 2 stejná čísla
print("Hodnoty od největší po nejmenší: {}".format(pole2))
