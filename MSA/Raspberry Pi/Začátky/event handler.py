from time import sleep

from gpiozero import LED, Button


def press():
    global led3, tlacitko
    led3.toggle()


tlacitko = Button(5, bounce_time=.05)
led1 = LED(26)
led2 = LED(19)
led3 = LED(13)

tlacitko.when_activated = press

try:
    while True:
        led2.off()
        led1.on()
        sleep(.5)
        led1.off()
        led2.on()
        sleep(.5)
except KeyboardInterrupt:
    led1.off()
    led2.off()
    led3.off()
