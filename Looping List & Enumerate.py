#Looping dari list
#For Loop
angka = [3,2,9,8,7,5,6]

for i in angka:
    print(f"Angka {i}")

#While Loop
panjang = len(angka)
i = 0
print(" ")
while i < panjang:
    print(f"Angka {angka[i]}")
    i += 1

#List Comprehension
print(" ")
[print(i) for i in angka]
print(" ")
[print(f"data : {i}") for i in angka]

kuadrat = [i**2 for i in angka]
print(kuadrat)

#Enumerate, dapat menampilkan indeks dan datanya
print("")
for index,data in enumerate(angka):
    print(f"Index ke-{index} memuat data {data}")