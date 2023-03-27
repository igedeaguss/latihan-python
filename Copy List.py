#Copy List
a = ['Sumatra', 'Jawa', 'Kalimantan','Papua']
print(a)

b = a.copy()
print(b)

#Mengetahui address data di list
print(f"Address a : {hex(id(a))}")
print(f"b: {b}")
print(f"Address b : {hex(id(b))}")

a[2] = 'Maluku'
print(a)
print(b)