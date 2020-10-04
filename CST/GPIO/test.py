from gpiozero import LED, Button

ledky = [LED(4), LED(17), LED(18), LED(27), LED(22), LED(23), LED(24), LED(25), LED(13), LED(19), LED(16), LED(20),
         LED(26), LED(21)]
tlacitko = Button(12)
tlacitko2 = Button(6)
while True:
    for i in ledky:
        input()
        i.value = 1
    input("Konec všech LED")
    for i in ledky:
        i.off()
