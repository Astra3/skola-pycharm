from time import sleep

from gpiozero import LED, Button
from DCBLP import T


def dekoder(a: int, b: int, c: int, d: int) -> list:
    """
    Převádí 4 bity z čítače na výsledných 14 bitů, jeden pro každou LED.
    :param a: 4. bit čítače
    :param b: 3. bit čítače
    :param c: 2. bit čítače
    :param d: 1. bit čítače
    :return: Pole o velikosti 14 bitů (hodnot), jeden pro každou LED
    """
    led = [not a and not b and not c and not d,
           a and b and c and d,
           a and b and c and not d,
           a and b and not c and d,
           a and b and not c and not d,
           a and not b and c and d,
           a and not b and c and not d,
           a and not b and not c and d,
           a and not b and not c and not d,
           not a and b and c and d,
           not a and b and c and not d,
           not a and b and not c and d,
           not a and b and not c and not d,
           not a and not b and c and d]
    return led


def main():
    # program nejprve inicializuje pole se 14 LED a 2 tlačítka, jedno pro reset a druhé pro blikání LED
    ledky = [LED(4), LED(17), LED(18), LED(27), LED(22), LED(23), LED(24), LED(25), LED(13), LED(19), LED(16), LED(20),
             LED(26), LED(21)]
    tlacitko = Button(12)
    reset_button = Button(6)

    # zde se vytvoří čítač, který je uložený celý v jednom poli
    citac = []
    for i in range(0, 4):
        citac.append(T())
    reset = 1  # je potřeba uvést reset na jeho počáteční hodnotu
    while True:
        # tohle jsou kroky pro čítač
        Y0 = citac[0].runTr(tlacitko.value, reset)[0]
        Y1 = citac[1].runTr(Y0, reset)[0]
        Y2 = citac[2].runTr(Y1, reset)[0]
        Y3 = citac[3].runTr(Y2, reset)[0]
        # zde se počítá reset, aby zresetoval obvod při dosažení 0010 u čítače, ale taky při zmáčknutí tlačítka
        reset = not (not Y3 and not Y2 and Y1 and not Y0)
        # TODO: První LED by se nemusela rozsvěcovat se zmáčknutím Reset
        reset = not reset_button.value and reset
        # případný print hodnot čítače
        # print(Y3, Y2, Y1, Y0)
        vysledek = dekoder(Y3, Y2, Y1, Y0)
        # zapíše v cyklu výsledek z dekodéru na všechny LED
        for i in range(0, 14):
            ledky[i].value = vysledek[i]
        # menší sleep ať se tolik nevytěžuje CPU
        sleep(.01)


if __name__ == '__main__':
    main()
