import os
import string
import random
#Template data siswa
siswa_template = {
    'id' : 'id',
    'nama':'nama',
    'alamat' : 'alamat',
    'nilai' : 'nilai'
}
nilai_siswa = {}
while True:
    os.system("cls")
    #membuat dict kosong dengan template kunci dari siswa_template
    siswa = dict.fromkeys(siswa_template.keys())
    siswa['id'] = input("ID Siswa : ")
    siswa['nama'] = input("Nama siswa : ")
    siswa['alamat']= input("Alamat siswa : ")
    siswa['nilai'] = int(input("Nilai siswa : "))
    
    #Buat random untuk setiap i dirange 6 
    key = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    nilai_siswa.update({key:siswa})
    print("\n")
    print(f"{'Kunci':<8} {'ID':<8} {'Nama':<15} {'Alamat':<16} {'Nilai':<5}")
    print('-'*59)
    for i in nilai_siswa:
        key = i
        Nama = nilai_siswa[key]['nama']
        Alamat = nilai_siswa[key]['alamat']
        Nilai = nilai_siswa[key]['nilai']
        ID = nilai_siswa[key]['id']
        print(f"{key:<8} {ID:<8} {Nama:<15} {Alamat:<16} {Nilai:<5}")
    
    print("\n")
    sudah = input("Ingin menambahkan data lagi (y/n): ")
    if sudah == 'n':
        break