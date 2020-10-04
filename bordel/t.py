print("Tento program slouží k zadávání čísel a nasldně tento pogram srovná podle velikosti")
pocet = int(input("zadej počet čísel, kolik ji chceš přidat: "))
cisla = [0] * pocet
vsechno = 0
while vsechno != pocet:
    cisla[vsechno] = int(input("zadej číslo: "))
    vsechno = vsechno + 1
# hodnoty [1, 5, 3], pocet = 3
start = 0  # ano nebo ne
prvni = 0  # počáteční index cyklu a třídění
zmena = 1  # 0
pocitadlo = 0  # 1
while start == 0:
    if pocitadlo == pocet:
        break
    else:
        zmena = 1
    while zmena == 1:
        if cisla[prvni] > cisla[prvni+1]:
            pom = cisla[prvni]
            cisla[prvni] = cisla[prvni+1]
            cisla[prvni+1] = pom
            pocitadlo = 0
        else:
            pocitadlo = pocitadlo+1
            zmena = 0
        prvni = prvni + 1
        if prvni + 1 == pocet:
            prvni = 0
cisla.reverse()
print(cisla)
