def func2(n):
 if n == 1:
     return [1]
 else:
     output = []
     previous = func2(n-1)
     length = len(previous)
     for i in range (0, length+1):
         if i in [0, length]:
             output.append(1)
         else:
             output.append(previous[i-1]+previous[i])
 return output

N = int(input("Masukkan Tinggi Segitiga : "))
for x in range (N):
    row = func2(x+1)
    print('  ' * (N-len(row)), end='')
    for y in row:
        print("{0:>3}".format(y), end=' ')
    print()
