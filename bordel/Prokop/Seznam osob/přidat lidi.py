file = open("osoby.txt", "a")
pocet = int(input("Kolik lidí si přejete přidat: "))

for i in range(pocet):
    jmeno = input("Jméno osoby: ")
    adresa = input("Přijímení osoby: ")
    cislo = input("Číslo osoby: ")
    mesto = input("Město osoby: ")
    file.write("{}, {}, {}, {}\n".format(jmeno, adresa, cislo, mesto))
file.close()
