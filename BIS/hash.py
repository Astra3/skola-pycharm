a = input("")
output = [ord(i) for i in a]
baf = 0
for i in output:
    baf += i
baf %= 256
print(hex((baf ^ 255) + 1))
