try:
    while True:  # tento loop pojišťuje kdyby uživatel zadal špatný počet
        zaci = int(input("Počet žáků (1-35): "))
        if zaci > 35:
            print("Počet žáků je nad 35.")
            continue
        elif zaci < 1:
            print("Žáků je méně jak 1.")
        else:
            break

    i = int(0)
    B = int(0)
    C = int(zaci)

    for i in range(1, zaci+1):
        A = input("Zadej známku pro {}. žáka.\n\"n\" nebo prázdno jako nepřítomen: ".format(i))
        try:
            A = int(A)  # zkusí převést A na integer
        except:
            None
        if A == "n" or A == "" or not 5 >= A >= 1 or A == str():  # kontroluje podmínky známky a absence
            if A == "n" or A == "":
                print("Žák {} chybí.".format(i))
                C = C - 1  # odečte žáka od celkového počtu
            else:
                print("Platné hodnoty jsou 1-5 a \"n\" nebo prázdno (jako nepřítomen).")
                i = i - 1  # umožní uživateli zadat hodnotu znovu
        else:
            B = B + A  # přičte známku k finálnímu dělení

    if C == 0:  # všichni žáci se od C odečetli, tedy by se pak dělilo nulou
        print("Všichni žáci chybí.")
    else:
        B = B / C
        print("Průměr známek: {}".format(B))
except TypeError:
    print("\nByla zadaná chybná hodnota.")
except KeyboardInterrupt:
    print("\nProgram ukončen z klávesnice.")
except ValueError:
    print("\nOd kdy je počet žáků slovo?")
