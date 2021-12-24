import random
n=int(input("Введите сколько чисел:"))
a=[random.randint(0,15) for i in range(n)]
print(a)
print(a[0])
print(a[-1])
s=1
for i in a:
    s*=i
print(s)
