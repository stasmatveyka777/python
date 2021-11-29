while True:
	age = int(input('Введите ваш возраст:   '))
	if age > 0:
		if age < 3:
		 	print('Билет бесплатный.')
		elif age >12:
		 	print('Билет стоит 12$.')
		else:
		 	print('Билет стоит 10$.')
	else: print('ERROR')