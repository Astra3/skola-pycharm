import time

import numpy as np


class Student:
    def __init__(self, jmeno: str, prijmeni: str, rok_narozeni: int, *znamky: int):
        self.__jmeno = jmeno
        self.__prijmeni = prijmeni
        year = int(time.ctime()[-4:])
        if rok_narozeni > year:
            print(f"Rok narození je vyšší než současný rok ({year}), nastavuji na současný rok.")
            self.__rok_narozeni = year
        else:
            self.__rok_narozeni = rok_narozeni
        self.znamky = znamky

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


s1 = Student("Karel", "Hnědkovský", 2021, 2, 3, 1, 2)
print(s1.prumer())
s1.znamky = (2, 3, 5)
print(s1.prumer())
