print("Tipe 1 : Pemyemprotan rumput / alang - alang         Rp250.000 / hektare\n")
print("Tipe 2 : Penyemprotan hama belalang                  Rp500.000 / hektare\n")
print("Tipe 3 : Penyemprotan kutu, hama, wereng             Rp750.000 / hektare\n")
print("Tipe 4 : Penyemprotan segala jenis hama dan rumput   Rp1.250.000 / hektare\n")
print("Data petani\n")
nama = input("Masukkan Nama Petani : ")
lahan = int(input("Masukkan Luas Lahan : "))
tipe = int(input("Masukkan Tipe Pemilihan : "))

if tipe == 1:
    biaya = lahan*25000
elif tipe == 2:
    biaya = lahan * 500000
elif tipe == 3:
    biaya = lahan * 750000
else:
    biaya = lahan * 1250000

if biaya >150000000 and lahan >100:
    diskon = biaya * 0.2
else:
    diskon = biaya * 0.1

total = biaya - diskon
print("Total Pembayaran Rp", biaya)
print("Diskon Rp", diskon)
print("Total Pembayaran Setelah Diskon Rp", total)