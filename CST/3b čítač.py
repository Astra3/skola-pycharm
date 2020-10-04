class RST:
    def __init__(self):
        self.Q = 0
        self.nQ = 1
        self.C_last = 0

    def runRST(self, S: int, R: int, C: int) -> list:
        V = not self.C_last and C
        # V = self.C_last and not C
        self.nQ = not (not (self.nQ and not (S and V)) and not (R and V))
        self.Q = not (not (self.Q and not (R and V)) and not (S and V))
        self.C_last = C
        return [self.Q, self.nQ]


class D(RST):
    def runD(self, D: int, C: int) -> list:
        self.Q, self.nQ = self.runRST(D, not D, C)
        return [self.Q, self.nQ]


class T(D):
    def runT(self, C: int) -> list:
        self.Q, self.nQ = self.runD(self.nQ, C)
        return [self.Q, self.nQ]


t0 = T()
t1 = T()
t2 = T()
while True:
    Y0 = t0.runT(int(input("C: ")))[0]
    Y1 = t1.runT(Y0)[0]
    Y2 = t2.runT(Y1)[0]
    print(Y2, Y1, Y0)
