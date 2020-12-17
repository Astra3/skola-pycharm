import numpy as np
from numpy import genfromtxt

vstup = open("vstupy/vstup.txt", "r")
vstup = vstup.readlines()
line = -1
ulohy = []
for i in range(0, int(vstup[0])):
    line += 2
    ulohy.append([[int(vstup[line].replace("\n", ""))]])
    cisla = vstup[line + 1].replace("\n", "").split(" ")
    temp = []
    for convert in cisla:
        temp.append(int(convert))
    ulohy[-1].append(temp)

pozice = 0
for i in ulohy:
    rozbit = False
    pozice_list = []
    index = -1
    # noinspection PyTypeChecker
    for cislo in i[1]:
        index += 1
        pozice = pozice2 = index
        pozice2 += i[1][pozice]
        pozice += i[1][pozice]
        while not(cislo >= i[0][0]):
            if pozice2 in pozice_list:
                break
            pozice_list.append(pozice2)
            while pozice > len(i[1]) - 1:
                pozice -= len(i[1])
            cislo += i[1][pozice]
            pozice2 += i[1][pozice]
            pozice += i[1][pozice]
        if cislo == i[0][0]:
            print("ANO")
            rozbit = True
            break
    if rozbit:
        continue
    else:
        print("NE")
