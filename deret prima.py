print("Program Cetak Deret Angka Prima")
batas = int(input("Masukkan batas : "))
for i in range (1, batas+1):
    bil = 0
    for j in range (1, batas+1):
        if (i%j == 0):
            bil = bil + 1
    if (bil == 2):
     print(i, end=" ")