a = int(input('Введите ваш вклад   '))
p = float(input('Введите %   '))
m = int(input('Введите месяц   '))
if m > 12:
    S = a + a * p / 100
    print(S)
else: print(a)
