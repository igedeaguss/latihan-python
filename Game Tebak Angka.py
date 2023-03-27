#Program membuat permainan tebak angka
import random

print("""Permainan Tebak Angka
Mode : 
1. Jawaban Random
2. Jawaban Tetap""")

pilih = int(input("Silahkan pilih mode (1 / 2) : "))

#untuk mendapatkan angka random 1 - 10
jawaban = random.randint (1,10)
coba = 0
#deklarasi jawaban tetap
jawabant = 8
print("="*20)
if pilih == 1: 
    print('Mode Jawaban Random!')
    while coba < 3:
     tebakan = int(input("Masukkan Tebakanmu (1 - 10) : "))

     if tebakan == jawaban:
       print("Tebakanmu Benar, Angka yang dimaksud", jawaban)
       break
     coba += 1
     if coba == 3:
      print("Yah, Kamu Gagal. Angka yang tersembunyi", jawaban)
      break
     
  
if pilih == 2:
    print("Mode Jawaban Tetap!")
    while coba < 3:
        tebakan = int(input("Masukkan Tebakanmu (1-10): "))
        
        if tebakan == jawabant:
            print('Yeay!, Kamu dapat menebaknya (Angka',jawabant,')')
            break
        coba +=1
        if coba == 3:
            print('Yah, Kamu Gagal!')
            break