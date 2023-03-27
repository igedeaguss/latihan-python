print("Usaha Angkutan Maju Jaya")
print("-"*30)
kode = input("Masukkan Kode Angkutan : ")
setor = int(input("Masukkan Jumlah Setoran : "))
if kode == "MI":
    print("Angkutan = Mikorlet")
    upah = 20000
    setorwjb = 40000
    persensupir = 0.7
    persenusaha = 0.3
    lebih = setor - (setorwjb+upah)
elif kode == "MB":
    print("Angkutan Mini Bus")
    upah = 25000
    setorwjb = 50000
    persensupir = 0.5
    persenusaha = 0.5
    lebih = setor - (setorwjb+upah)
elif kode == "TX":
    print("Angkutan Taksi")
    upah = 30000
    setorwjb = 70000
    persensupir = 0.6
    persenusaha = 0.4
    lebih = setor - (setorwjb+upah)

if lebih > 0:
    lebih = setor - (setorwjb+upah)
else:
    lebih = 0

bonussupir = persensupir*lebih
bonususaha = persenusaha *lebih
print("-"*30)
print("Kelebihan  Rp",lebih)
print("Bonus Supir  Rp",bonussupir)
print("Bonus Perusahaan  Rp",bonususaha)
print("Penghasilan Supir  Rp",upah+bonussupir)
print("Penghasilan Perusahaan Rp",setorwjb+bonususaha)
print("-"*30)