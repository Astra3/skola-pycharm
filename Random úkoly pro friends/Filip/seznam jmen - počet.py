pocet = int(input("Zadejte počet jmen: "))
jmena = []
for i in range(1, pocet + 1):
    jmeno = input(f"Zadejte {i}. jméno: ")
    jmena.append(jmeno)
print(f"Jména: {jmena}")
