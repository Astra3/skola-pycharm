jmeno = ""
jmena = []
while True:
    jmeno = input("Zadejte jméno: ")
    if jmeno == "konec":
        break
    jmena.append(jmeno)

print(f"Jména: {jmena}")
