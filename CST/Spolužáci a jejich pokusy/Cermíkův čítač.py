class RSTcko():
    def __init__(self):
        self.Q = 0
        self.nQ = 1
        self.C_predesle = 0

    def run_RST(self, S, R, C_aktual):
        C_aktual = not self.C_predesle and C
        T = not (S and R)
        S = T and S
        R = T and R
        self.nQ = not (not (self.nQ and not (S and C_aktual)) and not (R and C_aktual))
        self.Q = not (not (self.Q and not (R and C_aktual)) and not (S and C_aktual))
        self.C_predesle = C
        return [self.Q, self.nQ]

    def run_RST_reset(self, S, R, C, Reset):
        # V=(not self.C_predesle and C) or not Reset
        V = (self.C_predesle and not C) or not Reset
        self.nQ = not (not (self.nQ and not (S and V)) and not (R and V))
        self.Q = not (not (self.Q and not (R and V)) and not (S and V))
        self.C_predesle = C
        return [self.Q, self.nQ]


class Decko(RSTcko):
    def run_D(self, D, C):
        self.Q, self.nQ = self.run_RST(D, not D, C)
        return [self.Q, self.nQ]

    def run_D_reset(self, D, C, Reset):
        self.Q, self.nQ = self.run_RST_reset(D, not D, C, Reset)
        return [self.Q, self.nQ]


class T(Decko):
    def run_T(self, C):
        self.Q, self.nQ = self.run_D(self.nQ, C)
        return [self.Q, self.nQ]

    def run_T_reset(self, C, Reset):
        self.Q, self.nQ = self.run_D_reset(self.nQ and Reset, C, Reset)
        return [self.Q, self.nQ]


T_obvod_1 = T()
T_obvod_2 = T()
T_obvod_3 = T()
reset = 1
while True:
    Y0 = T_obvod_1.run_T_reset(int(input('C= ')), reset)[0]
    Y1 = T_obvod_2.run_T_reset(Y0, reset)[0]
    Y2 = T_obvod_3.run_T_reset(Y1, reset)[0]
    reset = not(not Y0 and Y1 and Y2)
    print(Y2, Y1, Y0)
