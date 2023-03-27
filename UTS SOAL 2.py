print("Perhitungan Berat Badan dengan Rumus Broca\n")
print("Pilihan : \n1. Pria \n2. Wanita\n")
pilih = int(input("Masukkan pilihan anda : "))
tinggi = int(input("Masukkan tinggi anda : "))

def beratbroca(tinggi):
  if pilih == 1 :
    beratideal = (tinggi - 100)-(0.1*(tinggi - 100))
  else : 
    beratideal = (tinggi - 100)-(0.15*(tinggi - 100))
  return beratideal

def beratnormal(tinggi):
  ratnormal = tinggi - 100
  return ratnormal
print("Berat normal anda ", beratnormal(tinggi))
print("Berat ideal anda ", beratbroca(tinggi))
