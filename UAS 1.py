print("Program Penentuan Gaji Karyawan Mingguan")
print("-"*40)
gol = int(input("Masukkan Golongan Karyawan : "))
jamker = int(input("Masukkan Jumlah Jam Kerja Karyawan : "))
if gol == 1:
  gapok = 100000
  gajijam = 5000
  lembur = 7500
elif gol == 2:
    gapok = 200000
    gajijam = 7000
    lembur = 10000
elif gol == 3:
    gapok = 300000
    gajijam = 9000
    lembur = 12500
else:
    gapok = 400000
    gajijam = 12000
    lembur = 15000

if jamker <= 40:
    togaj = gapok + (gajijam * jamker)
else:
    togaj = gapok + (gajijam * jamker) + lembur * (jamker - 40)
lembur = lembur * (jamker - 40)
print("Gaji Pokok Karyawan Golongan", gol,"adalah Rp",gapok)
print("Total Lembur Rp",lembur)
print("Total Gaji Karyawan Rp",togaj)