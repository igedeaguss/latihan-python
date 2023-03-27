import datetime as dt
#menampilakan tanggal hari ini
print(dt.date.today())
#menampilkan hari saat ini
hariIni = dt.date.today()
print(f"Saat ini hari {hariIni:%A}")

#menampilkan tanggal berdasarkan inputan
#Tahun, Bulan, Tanggal
Tanggal = dt.date(2021,9,12)
print(dt.date(2021,9,12))
print(f"Hari {Tanggal:%A}")

#menentukah hari berdasarkan inputan tanggal, bulan dan tahun
#menghitung umur
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

tgl = dt.date(tahun,bulan,tanggal)
umurHari = hariIni - tgl
umurTahun = umurHari.days//365
umurBulan = (umurHari.days % 365)//30

print(20*"-")
print("Tanggal saat ini",hariIni)
print("Tanggal yang dimasukkan adalah",tgl)
print(f"Hari {tgl:%A}")
print(f"Umur anda adalah {umurTahun} tahun {umurBulan} bulan")


