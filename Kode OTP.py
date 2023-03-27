import random

otp = random.randint(100,9999)
print(f'Kode OTP kamu {otp}')

user = int(input("Masukkan Kode OTP : "))
if user == otp:
    print("Hore! Berhasil")
else:
    print("Kodenya ga sama nih! Cek lagi yaa")