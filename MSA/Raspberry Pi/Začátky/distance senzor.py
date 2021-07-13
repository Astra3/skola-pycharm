import time

from gpiozero import DistanceSensor, LED, PWMLED
import numpy as np

dist = DistanceSensor(19, 13, max_distance=4)
led = PWMLED(16)

try:
    led.pulse(.5, .5, background=False)
except KeyboardInterrupt:
    led.close()
