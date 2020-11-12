from time import sleep

text = input("Zadejte text pro rolování: ")

pocet_znaku = 14
znak = "*"
text += znak * 11

while True:
    for i in range(0, len(text)):
        if i + pocet_znaku >= len(text):
            # FIXME když je před znakem hvězdička, tak znak se vypíše až poté, resp. nefunguje s malým počtem znak a
            #  krátkým textem
            print(f"\r{(text[i:] + text)[:pocet_znaku]}", end="", flush=True)
        else:
            print(f"\r{text[i:i + pocet_znaku]}", end="", flush=True)
        sleep(.5)
