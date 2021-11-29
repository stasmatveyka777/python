
while True:
	num = input('На сколько человек вы хотите забронировать столик?   ')
	if num == 'stop':
		print('Ок, я прекращаю')
		break
	else:
		if int(num) > 8:
			print('Вам прийдеться подождать.')
		else:
			print('Стол готов.')