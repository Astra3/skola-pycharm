from gpiozero import LED, Button
from time import sleep
from multiprocessing import Process

from typing import List

"""
Program pro blikání několika LED s 1-sekundovými intervaly s možností přerušení a opětovaného startu činnosti 
řízené přes tlačítko. Vyřešeno za pomoci několika procesů přes multiprocessing modul.
"""


def start(ledky2: List[LED]):
    """
    Funkce pro spuštění LED cyklu
    :param ledky2: List obsahující objekty LED, které se mají spustit
    """
    while True:
        for i2 in ledky2:
            i2.on()
            sleep(1)
            i2.off()


piny = (21, 20, 26, 16, 19, 13, 12, 6)  # tuple pinů LED
ledky = []
tlacitko = Button(5)
for i in piny:
    ledky.append(LED(i))  # vytvoří list objektů LED z výše zmíněných pinů
proces = Process(target=start, args=(ledky,))
proces.start()
while True:
    tlacitko.wait_for_active()
    if proces.is_alive():  # kontroluje zda proces již nebyl "ukončen"
        proces.kill()
        for i in ledky:
            i.off()
    else:
        proces = Process(target=start, args=(ledky,))  # objekt pro proces je potřeba znovu vytvořit (nelze spustit 2x)
        proces.start()
    tlacitko.wait_for_inactive()
    sleep(.01)  # s mými tlačítky vznikaly nepřesnosti při rychlém zmáčknutí
