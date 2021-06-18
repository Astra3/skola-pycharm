import time

from gpiozero import DistanceSensor, LED

dist = DistanceSensor(19, 13, max_distance=4)
led = LED(26)

while True:
    print(dist.distance)
    time.sleep(.2)
