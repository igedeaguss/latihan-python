print("Program Perhitungan Penjumlahan Deret")
print("-"*40)
print("pilihan :\n1. Deret Menurun\n2. Deret Menaik\n")
pilih = int(input("Masukkan pilihan : "))
if pilih == 1:
    a = int(input("Masukkan angka : "))
    total = 0
    for i in range (a, 0, -1):
        total = total + i
        if i == 1:
            print(i, "=", end = " ")
        else:
            print(i, "+", end = " ") 
    print(total)
else : 
    a = int(input("Masukkan angka : "))
    total = 0
    for i in range (1, a+1):
        total = total + i
        if i == a:
            print(i, "=", end = " ")
        else:
            print(i, "+", end = " ") 
    print(total)


