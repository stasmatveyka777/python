x = int(input('Введите х    '))
b = int(input('Введите b    '))
if x <= -2:
    if b >=0:
        answer = 3*x^2-8*b
    else:
        answer = -9*x^2-12*b
else:
    answer = 32 + x
print(answer)
