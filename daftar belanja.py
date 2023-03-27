n = int(input("Masukkan banyaknya barang : "))
total = 0
for i in range (1, n+1):
    print("Barang ke-", i)
    nabar = input("Masukkan nama barang : ")
    jumlah = int(input("Masukkan banyak barang : "))
    hasat = int(input("Masukkan harga satuan : "))
    juhar = jumlah * hasat
    print("Sub Total Rp",juhar)
    total += juhar   #total = total + juhar
    print("")
print("Total Belanjaan Rp", total)
