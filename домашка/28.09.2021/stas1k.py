import math

chose = input('Если хотите посчитать площадь по трем сторонам напишите "да", иначе напишите "нет" и мы будем считать по стороне и высоте ')
if (chose == 'да'):
	a = int(input('Введите  1-ую сторону '))
	b = int(input('Введите  2-ую сторону '))
	c = int(input('Введите  3-юю сторону '))
	p = (a+b+c)/2
	if (a+b > c) and (c+b > a) and (a+c > b):
		S = math.sqrt(p*abs(p-a)*abs(p-b)*abs(p-c))
		print("Площадь треугольника: ", S)
	else: print('Данного треугольника не существует')

elif (chose == 'нет'): 
	a = int(input('Введи сторону '))
	h = int(input('Введи высоту '))	
	if (a == 0) or (h == 0):print('ERROR')
	else:
			def square(a,h):
						return a*h/2
			print ('Площадь треугольника: ', square(a,h) )
else: print("ERROR")
