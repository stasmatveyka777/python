prompt = '\nПривет! Меня зовут БОТ, я хочу узнать о тебе все:'
prompt += "\nВведите 'out' для завершения программы"
prompt += "\nВведите ваше имя:   "
message = ""
while message != "out":
	message= input(f'\n{prompt}')
	print(f'Привет, круто что тебя {message}')