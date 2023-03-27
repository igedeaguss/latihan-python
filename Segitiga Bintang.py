tinggi = int(input("Masukkan tinggi bintang (0 untuk selesai) : "))

while tinggi != 0:
    maks = tinggi
    for bintang in range (0,tinggi):
        for pola in range (0, maks+1):
            print(" ",end="")
        for bentuk in range (0,bintang+1):
            print("* ",end="")
        maks-=1
        print("")
    tinggi = int(input("Masukkan tinggi bintang (0 untuk selesai) : "))

print("Terima Kasih!")