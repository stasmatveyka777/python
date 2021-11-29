x = int(input('Введите х:   '))
a = int(input('Введите a:   '))
if x > 0:
    if a < 0:
        y = 2*a*x
    else:
        y = a*x
else:
    y = 2
print(y)
