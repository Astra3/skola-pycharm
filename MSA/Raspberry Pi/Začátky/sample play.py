from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

buzz = TonalBuzzer(18)
frequency = 8000
period = frequency/60

with open("sample-data.txt", "r") as file:
    samples = file.readlines()

for sample in samples:
    buzz.value = float(sample.replace("\n", ""))
    sleep(period)

buzz.stop()
