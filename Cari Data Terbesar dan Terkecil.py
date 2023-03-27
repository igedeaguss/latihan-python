n = int(input("Masukkan banyaknya data : "))
bil = int(input("Masukkan data ke-1 : "))
max = bil
min = bil

for i in range (2, n+1):

    bil = int(input("Masukkan data ke-"+str(i)+": "))
    if bil > max:
        max = bil
    elif bil < min:
        min = bil
print("")
print("Data terbesar : ",max)
print("Data terkecil : ",min)