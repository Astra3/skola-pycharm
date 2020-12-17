from gpiozero import LED, Button

led: LED = LED(21)
tlacitko: Button = Button(20)
while True:
    tlacitko.wait_for_active()
    led.on()
    tlacitko.wait_for_inactive()
    led.off()
