print("Program Penentuan Rentang Angka\n")
angka = int(input("Masukkan Angka : "))

islebihdari0 = (angka > 0)
iskurangdari5 = (angka < 5)
islebihdari8 = (angka >8)
iskurangdari11 = (angka < 11)
#----0++++5-----8+++++11-----
hasil = (islebihdari0 and iskurangdari5) or (islebihdari8 and iskurangdari11)
print("Angka", angka,"bernilai", hasil,"pada rentang \nlebih dari 0 dan kurang dari 5 \natau \nlebih dari 8 dan kurang dari 11")

iskurangdari0 = (angka < 0)
islebihdari5 = (angka > 5)
iskurangdari8 = (angka < 8)
islebihdari11 = (angka > 11)
#++++0----5++++8-----11+++++
print("\n", 10*"-","\n")
hasil1 = (iskurangdari0 or islebihdari5) and (iskurangdari8 or islebihdari11)
print("Angka", angka,"bernilai", hasil1,"pada rentang \nkurang dari 0 atau lebih dari 5 \ndan \nkurang dari 8 atau lebih dari 11")