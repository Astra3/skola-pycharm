from time import sleep

# text = input("Zadejte text pro rolování: ")
text = "a"
pocet_znaku = 14
znak = "*"
text += znak * 8

while True:
    for i in range(0, len(text)):
        if i + pocet_znaku >= len(text):
            temp_text = text[i:] + text
            while len(temp_text) < pocet_znaku:
                temp_text += text
            print(f"\r{temp_text[:pocet_znaku]}", end="", flush=True)
        else:
            print(f"\r{text[i:i + pocet_znaku]}", end="", flush=True)
        sleep(.2)
