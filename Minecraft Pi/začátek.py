from mcpi.minecraft import Minecraft
from mcpi import block


def pricti(kolik_x=0, kolik_y=0, kolik_z=0):
    global pos
    pos = (pos[0] + kolik_x, pos[1] + kolik_y, pos[2] + kolik_z)


# TODO: Udělat kompresi, nejlépe RLE
abeceda = [
    "0111110100101001010001111",
    "1111110101101011010101110",
    "1111110001100011000110001",
    "1111110001100011000101110",
    "1111110101101011010110101",
    "1111110100101001000010000",
    "1111110001101011010110111",
    "1111100100001000010011111",
    "1000110001111111000110001",
    "0001100001000010000111111",
    "1111100100010101000110001",
    "1111100001000010000100001",
    "1111101000001000100011111",
    "1111101000001000001011111",
    "1111110001100011000111111",
    "1111110100101001010001000",
    "1111110001101011001111111",
    "1111110110101011010001000",
    "1110110101101011010110111",
    "1000010000111111000010000",
    "1111100001000010000111111",
    "1110000010000010001011100",
    "1111000001011100000111110",
    "1000101010001000101010001",
    "1100000100000110010011000",
    "1000110011101011100110001"
]
preklad = str.maketrans("áéíóúýčďěňřšťžů",
                        "aeiouycdenrstzu")

mc = Minecraft.create(address="192.168.88.118")
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
        for cislo in abeceda[ord(znak) - 97][0:25]:  # cislo = definice čísla nalezená v mapě, string
            if bool(int(cislo)):
                mc.setBlock(pos, 1)
            a += 1
            if a == 5:
                pricti(1, 5)  # další svislý řádek
                a = 0
            pricti(kolik_y=-1)  # o blok dolů v písmenu
        pricti(1)  # další písmeno
