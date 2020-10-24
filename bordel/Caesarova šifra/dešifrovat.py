"""Program na dešifrování Caesarovy šifry"""

slovo = input("Zadejte výraz k dešifrování: ").lower()
slovo.lower()
posun = 0 - int(input("Zadejte, o kolik se abeceda posunula při šifrování: "))
abeceda = "abcdefghijklmnopqrstuvwxyz"
minus = len(abeceda) - 1
while posun < 0 - minus:
    posun = posun + minus
sifra = ""
for i in range(0, minus + 1):
    sun = posun + i
    while sun > minus:
        sun = posun + i - minus
    sifra = sifra + abeceda[sun]
print(slovo.translate(str.maketrans(sifra, abeceda)))
