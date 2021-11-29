def greet_user(username):
	print(f'Привет, {username.title()}')
name = input('Введите ваше имя -->  ')
greet_user(name)