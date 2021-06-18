from gpiozero import PWMLED, Button
from time import sleep

led = PWMLED(20)
btn = Button(21)

i = 0

try:
    while True:
        btn.wait_for_active()
        led.value = i
        i += .01
        i %= .25
        sleep(.05)
finally:
    led.off()
