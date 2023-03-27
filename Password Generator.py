import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

all = lower + upper + numbers

panjang = 8
password = " ".join(random.sample(all,panjang))
print("Program Password Generator")
print('Password :',password)