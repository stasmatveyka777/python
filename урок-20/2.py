import random
x = int(input('x = '))
a = [random.randint(0,15)for j in range(x)]
print(a)
print(a[0], a[-1])
b = 1
for k in a:
    b = b*k
print(b)
