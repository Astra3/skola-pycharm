class RST():
    def __init__(self):
        self.Q = 0
        self.nQ = 1

    def run(self, S, R):
        C = not (S and R)  # přidáním tohoto řádku se odstranila potřeba pro C, inspirace ze strany skript 141
        self.nQ = not (not (self.nQ and not (S and C)) and not (R and C))
        self.Q = not (not (self.Q and not (R and C)) and not (S and C))
        return [self.Q, self.nQ]


class RS():
    def __init__(self):
        self.Q = 0
        self.nQ = 1

    def run(self, S, R):
        S, R = not(not S or R), not(not R or S)  # tohle řešení je inspirované ze strany 142 nahoře
        self.nQ = not (not (self.nQ and not S) and not R)
        self.Q = not (not (self.Q and not R) and not S)
        return [self.Q, self.nQ]


rst = RS()  # anebo rs = RST()
while True:
    s = int(input("S: "))
    r = int(input("R: "))
    # c = int(input("C: "))
    print(rst.run(s, r))
