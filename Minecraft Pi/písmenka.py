from mcpi.minecraft import Minecraft
from mcpi import block


def pricti(kolik_x=0, kolik_y=0, kolik_z=0):
    global pos
    pos = (pos[0] + kolik_x, pos[1] + kolik_y, pos[2] + kolik_z)


preklad = str.maketrans("áéíóúýčďěňřšťžů",
                        "aeiouycdenrstzu")

# TODO: Udělat kompresi, nejlépe RLE
with open("mapa.bin", "rb") as mapa:
    abeceda = "0" + bin(int(mapa.read().hex(), base=16)).lstrip("0b")  # převede bytearray do stringu binárních hodnot
mc = Minecraft.create(address="192.168.254.137")
x, y, z = mc.player.getPos()
pos = (x, y, z)
text = input("Zadejte vstupní text: ").lower()
pricti(kolik_y=10)
text = text.translate(preklad)
a = 0
if not text.replace(" ", "").isalpha():
    raise AttributeError("Nalezen nepodporovaný znak")
for znak in text:
    if znak == " ":
        pricti(3)
    else:
        pozice_znaku = (ord(znak) - 97) * 25
        for cislo in abeceda[pozice_znaku:pozice_znaku + 25]:  # cislo = definice čísla nalezená v mapě, string
            if bool(int(cislo)):
                mc.setBlock(pos, 1)
            a += 1
            if a == 5:
                pricti(1, 5)  # další svislý řádek
                a = 0
            pricti(kolik_y=-1)  # o blok dolů v písmenu
        pricti(1)  # další písmeno
