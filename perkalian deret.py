print("Program Hitung Faktorial")
print("")
b = int(input("Masukkan angka : "))
fakt = 1
print(b,"!")
for i in range (1, b+1):
    fakt = fakt * i
    if i == b:
        print(i, "=", end = " ")
    else:
        print(i, "x", end = " ")
print(fakt)