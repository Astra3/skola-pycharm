class RSTcko():
    def __init__(self):
        self.Q = 0
        self.nQ = 1

    def run_RST(self, S, R, C):
        T = not (S and R)
        S = T and S
        R = T and R
        self.nQ = not (not (self.nQ and not (S and C)) and not (R and C))
        self.Q = not (not (self.Q and not (R and C)) and not (S and C))
        return [self.Q, self.nQ]


class Decko(RSTcko):
    def run_D(self, D, C):
        self.Q, self.nQ = self.run_RST(D, not D, C)
        return [self.Q, self.nQ]


class Buffer(Decko):
    def __init__(self):
        super().__init__()
        self.Pole_D = []

    def pridani_obvodu(self, D, C):
        self.Pole_D.append(self.run_D(D, C)[0])


buffer = Buffer()
for x in range(0, 4):
    Da = int(input("D= "))
    C = int(input("C= "))
    buffer.pridani_obvodu(Da, C)
print(buffer)