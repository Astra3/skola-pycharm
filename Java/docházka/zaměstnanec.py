import time
from docházka.zařazení import Zarazeni


class Zamestnanec:
    def __init__(self, jmeno: str, prijmeni: str, zarazeni: Zarazeni, filepath="zaměstnanci/"):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._zarazeni = zarazeni
        self._dochazka = []
        try:
            self._file = open(f"{filepath}{self.jmeno} {self.prijmeni}.txt", "r")
            soubor = self._file.readlines()
            den = []
            for i in range(0, len(soubor) - 1, 2):
                den.append(soubor[i])
                den.append(soubor[i + 1])
                self._dochazka.append(den)
        except FileNotFoundError:
            pass
        finally:
            self._file = open(f"{filepath}{self.jmeno} {self.prijmeni}.txt", "a")
        self._den = []

    def prichod(self) -> str:
        if not len(self._den):
            self._den.append(time.time())
            return f"Příchod zadán na {time.ctime()}"
        else:
            return "Příchod nelze zadat dvakrát"

    def odchod(self) -> str:
        if len(self._den) == 1:
            self._den.append(time.time())
            # noinspection PyTypeChecker
            self._dochazka.append(self._den)
            self._den = []
            return f"Odchod zadán v {time.ctime()}"
        else:
            return "Odchod byl zadaný před příchodem"

    @property
    def dochazka(self) -> str:
        text = ""
        for dny in self._dochazka:
            prichod = time.ctime(float(dny[0]))
            try:
                odchod = time.ctime(float(dny[1]))
            except IndexError:
                odchod = "nezadáno"
            text += (f"Příchod: {prichod}\n"
                     f"Odchod: {odchod}\n"
                     f"{'*' * 5}\n")
        return text

    def __exit__(self, exc_type, exc_val, exc_tb):
        for i2 in self._dochazka:
            for i3 in i2:
                self._file.write(f"{i3}\n")
        self._file.close()

    def __enter__(self):
        return self

    @property
    def jmeno(self) -> str:
        return self._jmeno

    @property
    def prijmeni(self) -> str:
        return self._prijmeni

    @property
    def zarazeni(self) -> Zarazeni:
        return self._zarazeni
