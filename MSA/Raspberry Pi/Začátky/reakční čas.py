from gpiozero import PWMLED, Button
import time
from threading import Thread, Lock
import random
import logging

press = Button(20)
led = PWMLED(21)
zmacknuto: bool = press.value
inp = input("Name of the file to save data into: ")
time_pressed = 0
casy = []
pressed = False

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def button_press():
    global time_pressed, zmacknuto, lock
    while True:
        lock.acquire()  # locks here so main thread has to wait until button is pressed
        logger.debug("Locked")
        press.wait_for_inactive()  # wait for inactive button to not spam console
        press.wait_for_active()
        time_pressed = time.time()
        zmacknuto = True
        logger.debug("zmacknuto (pressed) changed to true")
        if lock.locked():
            lock.release()
            logger.debug("Unlocked")


thread = Thread(target=button_press, daemon=True, name="button press")
lock = Lock()
thread.start()
while True:
    print("Reaction countdown will begin in 3 seconds, hold button to stop.")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
        if press.is_active:
            break
    if press.is_active:
        break
    reakce = random.randint(1, 3) + random.random()
    zmacknuto = False
    print("Reaction time started")
    time.sleep(reakce)
    time_activated = time.time()
    if not zmacknuto:  # activates only if button was NOT pressed before the end of the countdown
        led.on()
        lock.acquire()  # lock here is acquired so that the thread waits until a button is pressed
        logger.debug("Locked")
        pressed = True
    reaction_time = time_pressed - time_activated  # computes reaction time
    if reaction_time < 0:
        print("Button was pressed too soon!")
    elif reaction_time > 0:
        print("Button was pressed.")
    print(f"Reaction time: {round(reaction_time, 2)}\n"
          f"Waiting time for LED: {round(reakce, 1)}")
    casy.append(reaction_time)
    led.off()
    if pressed:  # this releases the lock acquired above if button was NOT pressed before the end of the countdown
        lock.release()
        logger.debug("Unlocked")
        pressed = False

print(casy)

# reaction time saving, disabled for testing purposes
# casy2 = list(map(lambda x: str(x) + "\n", casy))
# with open(f"reakční časy/{inp}.csv", "a") as file:
#     file.writelines(casy2)
