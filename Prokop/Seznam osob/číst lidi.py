osoba = input("Zadejte adresu, jméno, přijímení nebo číslo hledaných osob: ")
soubor = open("osoby.txt", "r")
osoby = soubor.read()
osobyb = osoby.splitlines()
del osoby

for x in osobyb:
    pozice = x.find(osoba)
    if pozice != -1:
        jmeno = x.split(sep=", ")
        try:
            print("Jméno: {}\n"
                  "Přijímení: {}\n"
                  "Číslo: {}\n"
                  "Město: {}\n".format(jmeno[0], jmeno[1], jmeno[2], jmeno[3]))
        except IndexError:
            print("Údaje osoby jsou neúplné, smažte je manuálně ze souboru a přidejte je zpět pomocí přidání osob.\n"
                  'Obsah řádku osoby: "{}"'.format(x))
try:
    if jmeno == None:
        None
except:
    print('Nebyly nalezeny žádné výsledky na dotaz "{}"'.format(osoba))
