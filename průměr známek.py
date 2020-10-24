import pyperclip
import numpy as np


def zaokrouhli(vstup: np.ndarray) -> str:
    return np.format_float_positional(vstup, precision=4)


a = input("Enter pro clipboard, 'a' pro načtení ze známky.npy: ")
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
    print("Známky načteny ze souboru")


a2 = []
try:
    while True:
        a = input("Zadejte známku a za čárkou s mezerou váhu (1, 10), enter pro konec: ")
        if a == "":
            break
        else:
            a = a.split(", ")
        if len(a) != 2:  # checkuje zda vznikly jen dvě pole
            raise ValueError("Chybně zadaná známka")
        for i in a:
            if i[-1] == "-":  # kontroluje za je známka minus nebo ne
                a2.append(int(i[:-1]) + .5)
            else:
                a2.append(int(i))
        znamky = np.append(znamky, np.array([[a2[0]], [a2[1]]]), axis=1)
        a2 = []
    if a in "w":
        np.save("známky.npy", znamky)
        print("Soubor uložen")
except ValueError:
    print(f"Stala se chyba při zadávání známek, array uložen do souboru známky.npy")
    np.save("známky.npy", znamky)
finally:
    print(f"Výsledný array:\n"
          f"{znamky}\n"
          f"Medián: {zaokrouhli(np.median(znamky[0]))}\n"
          f"Aritmetický průměr: {zaokrouhli(np.mean(znamky[0]))}\n"
          f"Výsledný průměr: {zaokrouhli(np.average(znamky[0], weights=znamky[1]))}")
