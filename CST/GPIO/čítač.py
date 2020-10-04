from time import sleep

from gpiozero import Button, LED
from DCBLP import T


t0 = T()
t1 = T()
t2 = T()
tlacitko = Button(21)  # v závorkách jsou čísla pinů
tlacitko2 = Button(19)
led1 = LED(20)
led2 = LED(16)
led3 = LED(26)
reset = 1
while True:
    reset = tlacitko2.value
    Y0 = t0.runTr(tlacitko.value, reset)[0]  # value vrací hodnotu tlačítka, pokud zmáčknuté tak je 1
    Y1 = t1.runTr(Y0, reset)[0]
    Y2 = t2.runTr(Y1, reset)[0]
    led1.value = Y2  # value u LED svítí, když je 1
    led2.value = Y1
    led3.value = Y0
    sleep(.02)
