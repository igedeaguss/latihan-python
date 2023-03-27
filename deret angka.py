print("Program Menghitung Banyak Bilangan Bulat 1 - 100 yang habis dibagi 3 atau 5")
print()

batas = 100
banyak =banyak3=banyak5 = 0
bagi3=[]
bagi5=[]
for i in range (1, 100+1):
    if i % 3 == 0 or i % 5 == 0:
        banyak+=1
        print(i, end = " ")

    if i % 3 == 0:
        banyak3+=1
        bagi3.append(i)

    if i % 5 == 0:
        banyak5+=1
        bagi5.append(i)

print(" \n")
print('Himpunan bilangan yang habis dibagi 3 :')
print(bagi3,"= ",banyak3)
print()
print('Himpunan bilangan yang habis dibagi 5 :',bagi5,"=",banyak5)
print()
print("Jadi, ada",banyak,"buah bilangan yang habis dibagi 3 atau 5")
print()
