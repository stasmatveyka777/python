mes = int(input('Введите срок кредита (в месяцах):   '))
money = int(input('Введите сумму:   '))
perc = float(input('Введите годовой процент:   '))

for i in range(mes//12):
	money=money+money*perc/100
if mes%12 == 6:
	money=money+money*perc/200
	print(f'Вы получите1 {money}')
else:
	print(f'Вы получите {money}')
