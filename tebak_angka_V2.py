import random
angka = random.randint(1,10)
nyawa = 0
while True:
    tebakan = int(input("Masukkan tebakanmu (1-10): "))
    if tebakan != angka:
        print("Tebakanmu salah!")
        if tebakan > angka:
            print("Hints : Tebakanmu lebih besar")
        else:
            print("Hints : Tebakanmu lebih kecil")
    print(" ")
    if tebakan == angka:
        print("Tebakanmu benar!")
        break