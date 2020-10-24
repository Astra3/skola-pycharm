"""Program vypíše na obrazovku 'Úspěšný rok 2020 přeje Computer'
Třída Gratulant, objekt computer a metoda přání"""


class trida:
    def __init__(self):
        print("Ahoj Ráďo!")
    def ahoj(self):
        print("pápá")


class Gratulant:
    def prani(self):  # metoda
        """Popřeje vám nový rok 2020"""
        print("Úspěšný rok 2020 přeje Computer")

    def rada(self):  # metoda
        self.prani()
        print("Ahoj Ráďo")

    def __init__(self, a):
        """Tohle se vypíše vždy"""
        print(a)

    def ahoj(self, k):
        print("Ahoj kamaráde" + k)


computer = Gratulant("baf")  # computer = objekt
computer.ahoj("lek")
