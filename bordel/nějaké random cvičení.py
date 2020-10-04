f = open("soubor.txt", "r")
písmeno = input("Zadejte počáteční znak(y): ")
a = f.readlines()
p = 0
for i in a:
    if i[0:len(písmeno)] == písmeno:
        p += 1
        print(i.replace("\n", ""))
print(p)
