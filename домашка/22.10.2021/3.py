while True:
	num = input('Введите число:   ')
	if num == 'stop':
		print('Ок, я прекращаю.')
		break
	else:
		if int(num)%10 == 0:
			print('Число кратное 10')
		else:print('Число не кратное 10')