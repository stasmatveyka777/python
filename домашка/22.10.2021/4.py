i = 0
mylist = list()
vse = str()
while i <100:
	top = input('Введите топинг для пиццы:   ')
	if top == 'quit':
		break
	else: 
		mylist.append(top)
		vse = vse + mylist[i] + ', '
	i+=1

print(f'Ну и пицца получилась. И так вот все ингридиетны: {vse}')
