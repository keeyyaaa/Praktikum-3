MAX = int('0')

while True:
    x = int(input("Inputkan Bilangan x : "))
    if x == 0:
        break
    if x > MAX:
        MAX = x
print("Bilangan terbesar adalah :", MAX)
