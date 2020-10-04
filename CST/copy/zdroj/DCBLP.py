class Ako:
    def __init__(self):
        self.Q = 0

    def generate(self, s, t, CLK):
        s.enter(t, 1, self.generate, (s, t, CLK))
        self.Q = not self.Q
        CLK.put(self.Q)


class RS:
    """
    Spustí obvod RS, který funguje podle stavové tabulky ve skriptech na straně 137 (139 podle PDF).
    Obvod je ošetřen proti stavu, kdy R i S = 1.

    Ve stavu 1 (Q = 0) se drží, pokud je na S 0 a jakmile R = 0 a S = 1 přepne se se do stavu 2 (Q = 1).
    Ze stavu 2 se dostane, pokud R = 1 a S = 0.
    """
    def __init__(self):
        self.Q = 0
        self.nQ = 1

    def run(self, S: int, R: int) -> list:
        """
        :param S: Pokud je 1, přepne se z S1 do S2, pokud je 0 tak opačně
        :param R: Pokud je 0, přepne se z S1 do S2, pokud je 1 tak opačně
        :return: Vrací Q a nQ v listu
        """
        self.nQ = not (not R and not (not S and self.nQ))
        self.Q = not self.nQ
        return [self.Q, self.nQ]


class RST:
    """
    Funguje stejně jako :class:`RS`, akorát mění stav pouze když je na C náběžná hrana.
    NENÍ ošetřen proti stavu, kdy na S i R je 1 a na C náběžná hrana.

    Ve stavu 1 (Q = 0) se drží, pokud je na S 0 a jakmile R = 0 a S = 1 přepne se se do stavu 2 (Q = 1).
    Ze stavu 2 se dostane, pokud R = 1 a S = 0.
    """
    def __init__(self):
        self.Q = 0
        self.nQ = 1
        self.C_last = 0

    def runRST(self, S: int, R: int, C: int) -> list:
        """
        :param S: Pokud je 1, přepne se z S1 do S2, pokud je 0 tak opačně
        :param R: Pokud je 0, přepne se z S1 do S2, pokud je 1 tak opačně
        :param C: Přepne stav jen když je zde náběžná hrana
        :return: Vrací Q a nQ v listu
        """
        V = not self.C_last and C
        # V = self.C_last and not C
        self.nQ = not (not (self.nQ and not (S and V)) and not (R and V))
        self.Q = not (not (self.Q and not (R and V)) and not (S and V))
        self.C_last = C
        return [self.Q, self.nQ]

    def runRSTr(self, S: int, R: int, C: int, Reset: int) -> list:
        """RST, které je napsáno tak, aby fungovalo s T.runTr

        :func:`~DCBLP.RST.runRST`
        """
        V = (not self.C_last and C) or not Reset
        # V=(self.C_last and not C) or not Reset
        self.nQ = not (not (self.nQ and not (S and V)) and not (R and V))
        self.Q = not (not (self.Q and not (R and V)) and not (S and V))
        self.C_last = C
        return [self.Q, self.nQ]


class JK(RST):
    """
    Chová se podobně jako :class:`RST` reagující na náběžnou hranu, akorát je ošetřené proti stavu kdy je na obou vstupech 1.
    Druhý vstup v obou stavech ignoruje a přepíná se pouze pokud na C je náběžná hrana.

    Ve stavu 1 (Q = 0) setrvává, když J = 0 a jakmile J = 1, jde do stavu 2.
    Ve stavu 2 (Q = 1) setrvává, když K = 0 a přepne se když K = 1.
    """
    def runJK(self, J: int, K: int, C: int) -> list:
        """
        :param J: Jakmile je 1, přejde do stavu 2.
        :param K: Jakmile je 1, přejde do stavu 1
        :param C: To samé jak u :class:`RST`, aby obvod změnil stav musí zde být náběžná hrana
        :return: Vrací Q a nQ v listu
        """
        self.Q, self.nQ = self.runRST(J and self.nQ, K and self.Q, C)
        return [self.Q, self.nQ]


class D(RST):
    """
    Uloží do Q hodnotu D vždy když je náběžná hrana.
    Pokud na C náběžná hrana není, vrátí hodnotu Q.
    """
    def runD(self, D: int, C: int) -> list:
        """
        :param D: Hodnota kterou uložit
        :param C: Při náběžné hraně uloží D
        :return: Vrací Q a nQ v listu
        """
        self.Q, self.nQ = self.runRST(D, not D, C)
        return [self.Q, self.nQ]

    def runDr(self, D: int, C: int, Reset: int) -> list:
        """Obvod D napsaný tak, aby fungoval s T.runTr"""
        self.Q, self.nQ = self.runRSTr(D, not D, C, Reset)
        return [self.Q, self.nQ]


class T(D):
    """
    Obvod přepne stav vždy, když je na C náběžná hrana.
    Pokud na C náběžná hrana není, vrátí hodnotu Q.
    """
    def runT(self, C: int) -> list:
        """
        :param C: Vždy když je zde náběžná hrana, tak se hodnota Q přepne
        :return: Vrací Q i nQ v listu
        """
        self.Q, self.nQ = self.runD(self.nQ, C)
        return [self.Q, self.nQ]

    def runTr(self, C: int, Reset: int) -> list:
        """
        Zde aby obvod změnil stav, musí být Reset na 1

        :param C: Když je zde náběžná hrana a Reset je 0, tak se hodnota Q přepne
        :param Reset: Ovládá obvod. Když je 0 obvod se nikdy nepřepne
        :return: Vrací Q i nQ v listu
        """
        self.Q, self.nQ = self.runDr(self.nQ and T, C, Reset)
        return [self.Q, self.nQ]
