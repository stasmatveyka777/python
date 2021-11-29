import math

a = float(input('Есть уравнение x^2 = a. Введите а   '))
if a < 0 :
    xx = math.sqrt(abs(a))
    print(f'x = {xx}*i или -{xx}*i')
elif a == 0:
    print('x = ', a)
else:
    xx = math.sqrt(a)
    print(f'х = {xx} или -{xx}')
