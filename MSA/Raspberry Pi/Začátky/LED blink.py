from gpiozero import LED, Button
from time import sleep
from multiprocessing import Process

from typing import List


def start(ledky2: List[LED]):
    while True:
        for i2 in ledky2:
            i2.on()
            sleep(1)
            i2.off()


piny = (21, 20, 26, 16, 19, 13, 12, 6)
ledky = []
tlacitko = Button(5)
for i in piny:
    ledky.append(LED(i))
proces = Process(target=start, args=(ledky,))
proces.start()
run = True
while True:
    tlacitko.wait_for_active()
    if run:
        proces.kill()
        for i in ledky:
            i.off()
        run = False
    else:
        proces = Process(target=start, args=(ledky,))
        proces.start()
        run = True
    tlacitko.wait_for_inactive()
    sleep(.01)
