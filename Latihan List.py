#Program List Buku

daftar = []
while True :
    print("\nMasukkan Data Buku")
    judul = input("Judul Buku\t: ")
    penulis = input("Nama Penulis\t:")

    daftar.append([judul, penulis])

    lanjut =input("Ingin memasukkan data lagi? (y/n): ")

    if lanjut == "n":
        break

print("Data Buku")
#Membuat Tulisan menjadi rata tengah 
no = "No".center(2)
jdl = "Judul Buku".center(50)
nm = "Nama Penulis".center(50)
print(f"{no}|{jdl}|{nm}")

for index, buku in enumerate(daftar):
    #menampilkan index, judul buku, nama penulis dengan format rata kanan 50 karakter 
    print(f"{index+1:2}|{buku[0]:50}|{buku[1]:50}")