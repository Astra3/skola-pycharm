from docházka.zařazení import Zarazeni
from docházka.zaměstnanec import Zamestnanec

with Zamestnanec("Jan", "Novák", Zarazeni.inzenyr) as nekdo:
    print(f"Zadejte žádost pro uživatele {nekdo.jmeno} {nekdo.prijmeni}, Zařazení: {nekdo.zarazeni.value}\n"
          f"1 - zadejte příchod\n"
          f"2 - zadejte odchod\n"
          f"3 - vypíše docházku\n"
          f"0 - uloží do souboru a ukončí program")
    while True:
        a = input()
        if a == "1":
            return_value = nekdo.prichod()
        elif a == "2":
            return_value = nekdo.odchod()
        elif a == "3":
            return_value = nekdo.dochazka
        elif a == "0":
            break
        else:
            print("Špatně zadaná hodnota")
            continue
        print(f"\r{return_value}")
