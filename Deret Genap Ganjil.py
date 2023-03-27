print("Program Deret Genap Ganjil dengan Batas Angka")
print("---------------------------------------------")
n = int(input("Masukkan batas angka : "))

print("Deret genap dengan batas", n ,"adalah ")
total = 0
for i in range (2, n+1):
    if i % 2 == 0:
        print(i, end = " ")
        total = total + i
jml = 0
print("\nDeret ganjil dengan batas", n ,"adalah")
for a in range (1, n+1, 2):
     print(a, end = " ")
     jml = jml + a

print("\nHasil jumlah deret genapnya ", total)
print("Hasil jumlah deret ganjilnya ", jml)

print("Program Deret Ganjil Genap dengan Banyaknya Angka")
print("-------------------------------------------------")
a = int(input("Masukkan banyaknya deret : "))
print("Deret Ganjil")
for b in range(1, a+1):
    print(2*b-1, end=' ')
print()
print("Deret Genap")
for c in range (1, a+1):
    print(2*c, end= ' ')
print()