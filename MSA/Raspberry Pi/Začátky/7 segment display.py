from threading import Lock
from gpiozero import LED, Button


def zapsat(activated: Button):
    global ledky, cislo, hodnota
    for led, segment in zip(ledky, hodnota[cislo]):
        led.value = segment
    activated.wait_for_inactive()


def pridat(activated: Button):
    global cislo
    cislo += 1
    if cislo == 10:
        cislo = 0
    zapsat(activated)


def odebrat(activated: Button):
    global cislo
    cislo -= 1
    if cislo == -1:
        cislo = 9
    zapsat(activated)


vystupy = [4, 17, 18, 23, 24, 25, 5]
pricist = Button(20)
odecist = Button(21)
ledky = []
for i in vystupy:
    ledky.append(LED(i))

# dvourozměrné pole
hodnota = [[0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 1, 1, 1, 1],
           [0, 0, 1, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 1, 0],
           [1, 0, 0, 1, 1, 0, 0],
           [0, 1, 0, 0, 1, 0, 0],
           [0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0]
           ]

cislo = 0
pricist.when_activated = pridat
odecist.when_activated = odebrat
a = Lock()
try:
    a.acquire()
finally:
    a.release()
