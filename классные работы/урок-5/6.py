import math


a = int(input('Введите сторону треугольника   '))
r = int(input('Введите разиус вписаного круга   '))

if 6 == int((a*math.sqrt(3)/r)):
    print('Вписать можно')
else:
    print('Вписать нельзя, правильный радиус: ', int(a*math.sqrt(3)/6))
