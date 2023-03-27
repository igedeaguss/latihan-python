total = int(input("Total = "))
bentuk = input("Bentuk = ")

for i in range(total):
    print(format(bentuk*(i*2+1), '^30s'))
    