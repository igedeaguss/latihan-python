#Membuat banyak inputan dalam satu baris 
#dengan list comprehension

#Membuat dua inputan dalam satu baris
x,y = [int(x) for x in input("Masukkan nilai : ").split()]
print("Nilai Pertama ",x)
print("Nilai Kedua ",y)
print()
#Membuat tiga inputan dalam satu baris dengan spasi sebagai pemisah
x,y,z=[int(x) for x in input("Masukkan Nilai : ").split()]
print(f"Nilai pertama {x} | Nilai kedua {y} | Nilai ketiga {z}")
print()

#Membuat banyak inputan
x = [int(x) for x in input("Masukkan Nilai : ").split()]
print("Nilai : ",x)