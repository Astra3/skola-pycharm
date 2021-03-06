import pyperclip
import numpy as np


def zaokrouhli(vstup: np.ndarray) -> str:
    return np.format_float_positional(vstup, precision=4)


def vazeny_prumer(prumer: np.ndarray) -> str:
    return zaokrouhli(np.average(prumer[0], weights=prumer[1]))


a = input("Nic pro čtení z clipboard, 'a' pro načtení ze známky.npy, 'w' v kombinaci s předchozími pro uložení "
          "výsledného array: ")
if a in "w":
    data = pyperclip.paste()
    data = data.split("\n")
    data = [data[::5], data[4::5]]  # rozdělí array na známky a váhy
    secti = False
    znamky = []
    vahy = []
    for i in data[0]:  # změní známky na int a přičte .5 když je známka minus
        if i[-1] == "-":
            secti = True
        i = int(i[0])
        if secti:
            i += .5
            secti = False
        znamky.append(i)

    for i in data[1]:  # změní váhy na int
        i = int(i[0])
        vahy.append(i)
    znamky = np.array([znamky, vahy])
else:
    znamky = np.load("známky.npy")
    print(f"Známky načteny ze souboru\n"
          f"{znamky}")
print(f"Současný průměr: {vazeny_prumer(znamky)}")

a2 = []
try:
    while True:
        a3 = input("Zadejte známku a za čárkou s mezerou váhu (1, 10), enter pro konec: ")
        if a3 == "":
            break
        else:
            a3 = a3.split(", ")
        if len(a3) != 2:  # checkuje zda vznikly jen dvě pole
            raise ValueError("Chybně zadaná známka")
        for i in a3:
            if i[-1] == "-":  # kontroluje za je známka minus nebo ne
                a2.append(int(i[:-1]) + .5)
            else:
                a2.append(int(i))
        znamky = np.append(znamky, np.array([[a2[0]], [a2[1]]]), axis=1)
        print(f"Současný průměr: {vazeny_prumer(znamky)}")
        a2 = []
    if "w" in a:
        np.save("známky.npy", znamky)
        print("Soubor uložen")
except ValueError as exception:
    print(f"Chyba: {exception}")
    print(f"Stala se chyba při zadávání známek, array uložen do souboru známky.npy")
    np.save("známky.npy", znamky)
finally:
    print(f"Výsledný array:\n"
          f"{znamky}\n"
          f"Medián: {zaokrouhli(np.median(znamky[0]))}\n"
          f"Aritmetický průměr: {zaokrouhli(np.mean(znamky[0]))}\n"
          f"Výsledný průměr: {vazeny_prumer(znamky)}")
