from gpio import *
from time import *


def prevod(hodnota):
    return int(hodnota) * 1023


class RST():
    def init(self):
        self.Q = 0
        self.nQ = 1
        self.C_last = 0

    def runRST(self, S, R, C):
        V = not self.C_last and C
        self.nQ = not (not (self.nQ and not (S and V)) and not (R and V))
        self.Q = not (not (self.Q and not (R and V)) and not (S and V))
        self.C_last = C
        return [self.Q, self.nQ]


# tady bude trida T, ktera dedi ze tridy D
class T(RST):
    def runT(self, C):
        self.Q, self.nQ = self.nQ, C
        return [self.Q, self.nQ]


# tady je instance D1, tu uz potrebovat nebudeme

# tady bude instance T1
T1 = T()


def main():
    pinMode(0, IN)
    pinMode(1, OUT)
    print("Running")
    while True:
        T = digitalRead(0)
        C = digitalRead(0)
        vystup = T1.runT(C)
        print(prevod(vystup[0]))
        digitalWrite(1, prevod(vystup[0]))
        delay(1)


if name == "main":
    main()
