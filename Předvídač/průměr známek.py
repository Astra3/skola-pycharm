import pyperclip
import numpy as np
import datetime


def zaokrouhli(vstup: np.ndarray) -> str:
    return np.format_float_positional(vstup, precision=4)


def vazeny_prumer(prumer: np.ndarray) -> str:
    return zaokrouhli(np.average(prumer[0], weights=prumer[1]))


a = input("Nic pro čtení z clipboard, 'a' pro načtení ze známky.npy, 'w' v kombinaci s předchozími pro uložení "
          "výsledného array: ")
if "w" not in a:
    inp = pyperclip.paste()
    inp = inp.split("\n")
    data = [inp[::5], inp[4::5]]  # rozdělí array na známky a váhy
    if len(data[0]) != len(data[1]):
        data = [[], []]
        value: str
        pos: int
        current_pos = 0
        vaha = False

        for pos, value in enumerate(inp):
            if value.replace(".", "").replace("-", "").isnumeric() or (str(datetime.datetime.utcnow().year) in value or str(datetime.datetime.utcnow().year - 1) in value):
                if (current_pos == pos - 1 or current_pos == pos - 2) and vaha:
                    continue
                current_pos = pos
                if vaha:
                    data[1].append(value)
                    vaha = False
                elif not vaha:
                    data[0].append(value)
                    vaha = True

    znamky = []
    vahy = []
    for i in data[0]:  # změní známky na int a přičte .5 když je známka minus
        num = int(i[0])
        if i[-1] == "-":
            num += .5
        znamky.append(num)

    for i in data[1]:  # změní váhy na int
        if i[0:2] == "10":
            i = 10
        else:
            i = int(i[0])
        vahy.append(i)
    znamky = np.array([znamky, vahy])
else:
    znamky = np.load("známky.npy")
    print(f"Známky načteny ze souboru\n"
          f"{znamky}")
a2 = []
try:
    print("Tipy a triky:\n"
          "'d' pro smazání poslední známky\n"
          "'z' pro zobrazení současných známek")
    print(f"Současný průměr: {vazeny_prumer(znamky)}")

    while True:
        a3 = input("Zadejte známku a za mezeru váhu (1 10), enter pro konec: ")
        if a3 == "":
            break
        elif a3 == "d":
            znamky = np.delete(znamky, -1, 1)
            print("Známka smazána")
        elif a3 == "z":
            print(znamky)
        else:
            a3 = a3.split(" ")
            if len(a3) != 2:  # checkuje zda vznikly jen dvě pole
                raise ValueError("Chybně zadaná známka")
            for i in a3:
                if i[-1] == "-":  # kontroluje za je známka minus nebo ne
                    a2.append(int(i[:-1]) + .5)
                else:
                    a2.append(int(i))
            znamky = np.append(znamky, np.array([[a2[0]], [a2[1]]]), axis=1)
            a2 = []
        print(f"Současný průměr: {vazeny_prumer(znamky)}")
    if "w" in a:
        np.save("známky.npy", znamky)
        print("Soubor uložen")
except (ValueError, IndexError) as exception:
    print(f"Chyba: {exception}")
    print(f"Stala se chyba při zadávání známek, array uložen do souboru známky.npy")
    np.save("známky.npy", znamky)
finally:
    print(f"Výsledný array:\n"
          f"{znamky}\n"
          f"Medián: {zaokrouhli(np.median(znamky[0]))}\n"
          f"Aritmetický průměr: {zaokrouhli(np.mean(znamky[0]))}\n"
          f"Výsledný průměr: {vazeny_prumer(znamky)}")
