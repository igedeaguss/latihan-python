#Latihan membuat segitiga 

sisi = 10
#dummy variable
count = 1
for i in range(sisi):
    print("* "*count)
    count += 1
print(" ")
count = 1
spasi = int(sisi/2)

#print segitiga sama sisi
while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -=1
        count+=1
    else:
        #akan kembali ke atas jika ganjil 
        count+=1
        continue
    #akan break jika count melebihi sisi
    if count > sisi:
        break
