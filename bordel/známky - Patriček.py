známka=0
student=int(input("počet studentů: "))
if (student > 35 or student == 0):
    print("Chybný počet studentů")
else:
    for z in range(student):
        z = input("Zadej známku: ")
if (známka == "n"):
    print("Student nepsal.")
if (známka > 0 or známka < 6):
    print("Špatná známka.")
else:
    prumer == známka / student
    print("Průměr je: ")
input()
