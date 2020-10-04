# /usr/bin/python3
from math import pi


def obsah_kruhu(polomer):
    """Tato funkce počítá obsah kruhu"""
    obsah = pi * polomer**2
    return obsah


def objem_valce(vyska, polomer):
    """Tato funkce počítá objem kruhu na základě obsahu"""
    objem = obsah_kruhu(polomer) * vyska
    return objem


try:  # try je zde jako pojistka proti nečíselným hodnotám
    print('"obsah" pro obsah kruhu\n'
          '"objem" pro objem válce\n')
    pocitat = input()
    if pocitat == "objem":
        polomer = float(input("Zadejte poloměr válce: "))
        vyska = float(input("Zadejte výšku válce: "))
        print("Objem válce je {}".format(objem_valce(vyska, polomer)))
    elif pocitat == "obsah":
        polomer = float(input("Zadejte poloměr kruhu: "))
        print("Obsah kruhu je {}".format(obsah_kruhu(polomer)))
    else:
        print("Byla zadána špatná hodnota")
except ValueError:
    print("Hodnoty musí být pouze číselné, pro desetiny použijte tečku.")
except KeyboardInterrupt:
    print("Program ukončen z klávesnice.")
