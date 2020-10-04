cislo = 0  # jedna ze základních proměnných pro násobení
while cislo != 10:  # cyklus se ukončí jakmile hlavní číslo dosáhne nuly
    cislo = cislo + 1
    cislo1 = 0
    while cislo1 != 10:
        cislo1 = cislo1 + 1
        print("{}*{}={}".format(cislo, cislo1, cislo * cislo1), end="\t")
    print()
