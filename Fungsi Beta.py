print("Program Hitung Fungsi Beta")
print("-"*30)
a = int(input("Masukkan Nilai a : "))
b = int(input('Masukkan Nilai b : '))
Ga = a - 1
Gb = b - 1
jml = a + b
Gjml = jml - 1

faktor = 1
for i in range(1, Ga+1):
    faktor= faktor*i

faktorb = 1
for j in range (1, Gb+1):
    faktorb = faktorb * j

faktorj = 1
for k in range(1, Gjml+1):
    faktorj = faktorj * k

beta = (faktor * faktorb) / faktorj

print("Nilai fungsi beta dari",a,",",b,"adalah", beta)
print("B(",a,",",b,") = ",beta)
