from gpiozero import Button, LED

tlacitko = Button(21)
cervena = LED(13)

i = 0
while True:
    tlacitko.wait_for_active()
    i += 1
    if i == 11:
        cervena.toggle()
        i = 0
    tlacitko.wait_for_inactive()
