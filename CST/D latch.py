class RST:
    def __init__(self):
        self.Q = 0
        self.nQ = 1

    def run(self, S, R, C):
        self.nQ = not (not (self.nQ and not (S and C)) and not (R and C))
        self.Q = not (not (self.Q and not (R and C)) and not (S and C))
        return [self.Q, self.nQ]


class D(RST):
    def runD(self, In, C):
        self.Q, self.nQ = self.run(In, not In, C)
        return [self.Q, self.nQ]


decko = D()
while True:
    In = int(input("In: "))
    c = int(input("C: "))
    print(decko.runD(In, c))
