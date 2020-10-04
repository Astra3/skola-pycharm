from gpiozero import Button, LED
from DCBLP import T

t0 = T()
t1 = T()
t2 = T()
t3 = T()

tlacitko = Button(21)  # v závorkách jsou čísla pinů
cervena = LED(13)
tecko = T()
reset = 1
while True:
    Y0 = t0.runTr(tlacitko.value, reset)[0]  # value vrací hodnotu tlačítka, pokud zmáčknuté tak je 1
    Y1 = t1.runTr(Y0, reset)[0]
    Y2 = t2.runTr(Y1, reset)[0]
    Y3 = t3.runTr(Y2, reset)[0]
    reset = not(not Y3 and Y2 and not Y1 and Y0)
    cervena.value = tecko.runT(not reset)[0]
    # False True False True

