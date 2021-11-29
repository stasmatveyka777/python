while True:
	k = int(input('Введите k (не более 15):  '))
	if k <=15: break
p = 1
i = 1
while True:
	p*=i 
	i+=1
	if i>k:break
print (f'Фактариал числа равен: {p}')