from random import randint


class RST:
    def __init__(self):
        self.Q = 0
        self.nQ = 1

    def run(self, S, R, C):
        self.nQ = not (not (self.nQ and not (S and C)) and not (R and C))
        self.Q = not (not (self.Q and not (R and C)) and not (S and C))
        return [self.Q, self.nQ]


class D(RST):
    def runD(self, In, C=1):
        self.Q, self.nQ = self.run(In, not In, C)
        return [self.Q, self.nQ]


bit = 4  # počet bitů v bufferu, nastavitelná hodnota
decko = list()
for i in range(0, bit):
    decko.append(D())
    # první řádek zde je pro automatické plnění pomocí modulu random, druhý je pro manuální hodnoty
    decko[i].runD(randint(0, 1))  # naplníme všechny obvody náhodnou hodnotou
    # decko[i].runD(int(input("{}. obvod: ".format(i+1))))  # zde je třeba zmínit, že první vypsaná hodnota je již posunutá o 1 takt

while True:
    """Zde je třeba použít trochu workaround, aby to fungovalo
    Funguje to tak, že se uloží hodnota posledního déčka, proběhne cyklus který aktualizuje všechny déčka až na první,
    a po dokončení cyklu se aktualizuje obvod první (index 0)"""
    temp = decko[-1].runD(0, 0)[0]
    for i in reversed(range(1, bit)):
        decko[i].runD(decko[i-1].runD(0, 0)[0])
    decko[0].runD(temp)

    for i in decko:
        print(i.runD(0, 0)[0])
    input("Enter pro takt")
