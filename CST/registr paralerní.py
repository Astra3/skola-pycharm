from DCBLP import D
from random import randint


class REG(D):
    def __init__(self, b):
        super().__init__()
        self.d = [D() for _ in range(0, b)]
        self.b = b

    def runREGp(self, D, C):
        Y = [0] * self.b
        for i in range(0, self.b):
            Y[i] = self.d[i].runD(D[i], C)[0]
        return Y

    def runREGs(self, D, C):
        Y = [None] * self.b
        for i in range(self.b - 1, 0, -1):
            Y[i] = self.d[i].runD(self.d[i - 1].Q, C)[0]
        Y[0] = self.d[0].runD(D, C)[0]
        return Y


b = int(input("Zadejte počet hodnot: "))
a = REG(b)
while True:
    Cn = int(input("Zadejte C: "))
    hodnoty = list()
    while len(hodnoty) < b:
        hodnoty.append(randint(0, 1))
    y = a.runREGs(hodnoty, Cn)
    print(y)
