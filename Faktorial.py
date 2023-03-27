print("Program Faktorial")
print("-----------------")
n =  int(input("Masukkan angka : "))
faktor = 1
for i in range(1, n+1):
    print(i, end=' ')
    faktor = faktor*i
print("")
print(n,"! =",faktor)