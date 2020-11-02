import time
import numpy as np


class Adresa:
    def __init__(self, ulice: str, cislo_popisne: int, mesto: str, psc: str):
        """
        Třída pro adresu
        :param ulice: ulice
        :param cislo_popisne: číslo popisné
        :param mesto: město
        :param psc: PSČ
        """
        self.ulice = ulice
        self.cislo_popisne = cislo_popisne
        self.mesto = mesto
        self.psc = psc

    @property
    def psc(self) -> int:
        return self._psc

    @psc.setter
    def psc(self, psc: str):
        """
        Setter nastavující PSČ
        :raises KeyError: když je zadané neplatné PSČ
        :param psc: PSČ
        """
        psc = psc.replace(" ", "")
        if len(psc) != 5 and psc.isdecimal():
            raise KeyError("PSČ je neplatný formát")
        else:
            self._psc = int(psc)


class Student(Adresa):
    def __init__(self, jmeno: str, prijmeni: str, rok_narozeni: int, ulice: str, cislo_popisne: int, mesto: str,
                 psc: str, *znamky: int):
        """
        Třída pro studenta
        :param jmeno: jméno studenta
        :param prijmeni: příjmení studenta
        :param rok_narozeni: rok narození studenta
        :param ulice: ulice, kde student žije
        :param cislo_popisne: studentovo číslo popisné
        :param mesto: město, kde student žije
        :param psc: PSČ studentova města
        :param znamky: seznam známek studenta
        """
        super().__init__(ulice, cislo_popisne, mesto, psc)
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rok_narozeni = rok_narozeni
        self.znamky = znamky

    @property
    def rok_narozeni(self):
        return self._rok_narozeni

    @rok_narozeni.setter
    def rok_narozeni(self, rok_narozeni):
        year = int(time.ctime()[-4:])
        if rok_narozeni > year:
            print(f"Rok narození je vyšší než současný rok ({year}), nastavuji na současný rok.")
            self._rok_narozeni = year
        else:
            self._rok_narozeni = rok_narozeni

    @property
    def znamky(self) -> np.ndarray:
        return self._znamky

    @znamky.setter
    def znamky(self, znamky: tuple):
        """
        NumPy array uchovávající známky
        :param znamky: tuple známek
        :raise KeyError: při jiných známkách než 1-5
        """
        znamky = np.array(znamky)
        if znamky.max(initial=5) > 5 or znamky.min(initial=1) < 1:
            raise KeyError("Jedna známka byla vyšší jak 5 nebo menší jak 1")
        else:
            self._znamky = znamky

    def prumer(self) -> int:
        """
        Spočítá a vrátí průměr
        :return: průměr známek
        """
        return np.average(self._znamky)


s1 = Student("Karel", "Hnědkovský", 2021, "Masarykova", 756, "Praha", "756 01", 2, 1, 5, 3, 2)
# print(s1.prumer())
# s1.znamky = (2, 3, 5)
print(s1.jmeno)
print(s1.prijmeni)
print(s1.rok_narozeni)
print(s1.ulice)
print(s1.cislo_popisne)
print(s1.mesto)
print(s1.psc)
print(s1.znamky)
print(s1.prumer())
