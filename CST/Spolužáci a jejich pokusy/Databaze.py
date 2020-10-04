jmena = []
cisla = []

pocet = int(input("Zadej počet údajů: "))

for a in range(pocet):
    jmena.append(input("Zadej jméno: "))

for b in range(pocet):
    cisla.append(input("Zadej číslo: "))

while True:
    poradove_cislo = int(input("Zadej pořadové číslo: ")) - 1
    if poradove_cislo == -1 or poradove_cislo > pocet - 1:
        print("neexistuje")
    else:
        print(jmena[poradove_cislo], " ", cisla[poradove_cislo])
