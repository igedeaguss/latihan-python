banyak = banyak4 = banyak5 = 0
b = a = c = 0
himpu4 = []
himpu5 = []
himpu45 = []
banyak4aja = banyak5aja = []

for i in range(101, 600+1):
    if i % 4 == 0 and i % 5 == 0:
     himpu45.append(i)
     banyak+=1

    if i % 4 == 0 and i % 5 != 0:
         banyak4aja.append(i)
         b+=1

    if i % 5 == 0 and i % 4 != 0:
        banyak5aja.append(i)
        a+=1

    if i % 4 ==0:
        banyak4+=1
        himpu4.append(i)

    if (i % 5 ==0):
        banyak5+=1
        himpu5.append(i)

print("Himpunan bilangan yang habis dibagi 4 dan 5")
print(himpu45,"=",banyak,"\n")
print("Himpunan bilangan yang habis dibagi 4")
print(himpu4,"=",banyak4,"\n")
print("Himpunan bilangan yang habis dibagi 5")
print(himpu5,"=",banyak5)
print("\nHimpunan bilangan yang hanya habis dibagi 4 saja")
print(banyak4aja, "=", a)
print("\nHimpunan bilangan yang hanya habis dibagi 5 saja")
print(banyak5aja, "=", b)
