#Manipulasi List / Operasi pada List

data1= ["Jakarta","Bandung","Medan","Denpasar"]
print(data1)

#mengambil data list
ambil = data1[0]
print(f"Data pertama yang ada di list adalah {ambil}")

#Mengambil data yang paling akhir
akhir = data1[-1]
print(f"Data terakhir yang ada di list adalah {akhir}")

#Mengambil info jumlah data list
banyak = len(data1)
print(f"Banyaknya data = {banyak}")

#Menambahkan data / item sesuai posisi
print(f"Item list sebelum diubah = {data1}")

#Formatnya data1.insert(posisi/indeks, item/data)
data1.insert(2,"Banyuwangi")
print(f"Item list sesudah diubah = {data1}")

#Menambah item di akhir list
data1.append("Kupang")
print(f"Item list sesudah diubah lagi = {data1}")

#Menggabungkan dua list 
data2 = ["Banjarmasin","Manado","Lombok"]
data1.extend(data2)
print(f"Hasil Gabungan List = {data1}")

#Merubah data / item pada list
data1[1] = "Semarang"
print(f"List Baru  = {data1}")

#Menghapus item
data1.remove("Semarang")
print(f"Data Remove = {data1}")

#Menghapus item paling belakang
data1.pop()
print(f"Data pop = {data1}")