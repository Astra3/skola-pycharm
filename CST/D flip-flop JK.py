# využívá přímého importu třídy z modulu DCBLP.py
from DCBLP import JK


# class RST:
#     def __init__(self):
#         self.Q = 0
#         self.nQ = 1
#         self.C_last = 0
#
#     def runRST(self, S, R, C):
#         V = not self.C_last and C
#         # V = self.C_last and not C
#         self.nQ = not (not (self.nQ and not (S and V)) and not (R and V))
#         self.Q = not (not (self.Q and not (R and V)) and not (S and V))
#         self.C_last = C
#         return [self.Q, self.nQ]
#
#     def runRSTr(self, S, R, C, Reset):
#         V = (not self.C_last and C) or not Reset
#         # V=(self.C_last and not C) or not Reset
#         self.nQ = not (not (self.nQ and not (S and V)) and not (R and V))
#         self.Q = not (not (self.Q and not (R and V)) and not (S and V))
#         self.C_last = C
#         return [self.Q, self.nQ]
#
#
# class JK(RST):
#     def runJK(self, J, K, C):
#         self.Q, self.nQ = self.runRST(J and self.nQ, K and self.Q, C)
#         return [self.Q, self.nQ]


class D(JK):
    def runD(self, In, C):
        self.Q, self.nQ = self.runJK(In, not In, C)
        return [self.Q, self.nQ]


d = D()
while True:
    Ina = int(input("In: "))
    c = int(input("C: "))
    print(d.runD(Ina, c))
