#allternatif membuat List
#Membuat list deret angka 1 - 9
data_range = range(0, 10) 
data_list = list(data_range)
print(data_list)

#Membuat list deret angka dengan step 2
data_range = range(0, 10, 2) #(start, stop, step)
data_list1 = list(data_range)
print(data_list1)

#List dengan for loop
data_list2 = [i for i in range(0,10)]
print(data_list2)

data_list3 = [i**2 for i in range(0,10)]
print(data_list3)

#List pake for if 
data_list4 = [i for i in range(0, 10) if i%2 == 0]
print(data_list4)