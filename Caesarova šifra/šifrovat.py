"""Program na šifrování přes fucking Caesarovu šifru, f u, anglická abeceda only"""

slovo = input("Zadejte výraz k zašifrování: ").lower()
posun = 0 - int(input("Zadejte, o kolik se má abeceda posunout: "))
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
print(slovo.translate(str.maketrans(abeceda, sifra)).upper())
