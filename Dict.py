n = int(input("Masukkan banyaknya data : "))
data = {}
for i in range(1, n+1):
    print(f"Data ke-{i}")
    nama = input("Masukkan Nama : ")
    nilai = int(input("Masukkan Nilai Rata - rata : "))
    data[nama]=nilai #Memasukkan inputan data ke dicionary. Nama sebagai kunci dan nilai sebagai isi dari kunci
    print("")

#Menampilkan data pada dictionary
print(f"Daftar Siswa : \n{data}")

print("Nilai rata - rata : ")
#Perintah untuk menampilkan nilai
for a in data:
    print(data[a])
print("")

#Menampilkan kunci dan nilai
print("Daftar Siswa")
print("="*20)
for b in data:
    print(b, "=",data[b])