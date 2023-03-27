data1 = [7,9]
data2 = [3,6]

data2D = [data1, data2]

print(f"Data : {data2D}")

#Cara mengambil data di nested list
data = data2D[0]
print(f"Data : {data}")
data01 = data2D[0][1]
print(f"Data : {data01}")
data10 = data2D[1][0]
print(f"Data : {data10}")

#Cara memakai Deepcopy
from copy import deepcopy

data2D_deep = deepcopy(data2D)

print(f"address list asli : {hex(id(data2D))}")
print(f"address deep copy : {hex(id(data2D_deep))}")

print("\nAddress dari member ke-1")
print(f"Address list asli : {hex(id(data2D[0]))}")
print(f"Address deep copy : {hex(id(data2D_deep[0]))}")
#Kesimpulannya jika ingin mengcopy nested list maka gunakanlah deepcopy