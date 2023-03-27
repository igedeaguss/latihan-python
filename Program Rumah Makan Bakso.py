from time import strftime
print("Rumah Bakso Enak")
print("-"*20)
print("""Menu Makanan : 
1. Bakso    Rp 12000
2. Mie Ayam Rp 13000""")
print("""
Menu Minuman : 
3. Air Mineral Rp 3000
4. Es Teh      Rp 4000
5. Es Jeruk    Rp 5000""")
print("")
total = 0
cacah = 0
#deklarasi nilai awal
bakso = tbakso = 0
ayamm = tayam = 0
air = tair = 0
teh = tteh = 0
jeruk = tjeruk = 0

pilih = int(input("Masukkan pilihan makanan atau minuman (0 untuk selesai) : "))
while pilih != 0:
    if pilih == 1:
        bakso = int(input("Masukkan banyaknya porsi bakso   : "))
        tbakso = bakso * 12000
        total = total + tbakso
        cacah = cacah + bakso
    elif pilih == 2:
        ayamm = int(input("Masukkan banyaknya porsi mie ayam :"))
        tayam = ayamm * 13000
        total = total + tayam
        cacah = cacah + ayamm
    elif pilih == 3:
        air = int(input("Masukkan banyaknya air mineral     : "))
        tair = air * 3000
        total = total + tair
        cacah = cacah + air
    elif pilih == 4:
        teh = int(input("Masukkan banyaknya es teh          : "))
        tteh = teh * 4000
        total = total + tteh
        cacah = cacah + teh
    else : 
        jeruk = int(input("Masukkan banyaknya es jeruk      : "))
        tjeruk = jeruk * 5000
        total = total + tjeruk
        cacah = cacah + jeruk
    pilih = int(input("Masukkan pilihan makanan atau minuman (0 untuk selesai) : "))

print(f"Total Pembayaran Rp{total:,}")
bayar = int(input("Tunai : "))
kembali = bayar - total
print("")
print("Daftar Pesanan")
#menampilkan tanggal dan waktu hari ini 
print("Tanggal",strftime("%d-%m-%Y %H:%M:%S"))
print("="*50)
if bakso != 0:
 print(f"Bakso       {bakso} porsi  Rp{tbakso:,}")
if ayamm != 0:
 print(f"Mie Ayam    {ayamm} porsi  Rp{tayam:,}")
if air != 0:
 print(f"Air Mineral {air} botol  Rp{tair:,}")
if teh !=0:
 print(f"Es teh      {teh} gelas  Rp{tteh:,}")
if jeruk != 0:
 print(f"Es Jeruk    {jeruk} gelas Rp{tjeruk:,}")

print("="*50)
print("Total Item",cacah)
print(f"Total Pembayaran   Rp{total:,}")
print(f"Tunai              Rp{bayar:,}")
print(f"Kembali            Rp{kembali:,}")


