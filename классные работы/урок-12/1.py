# def pizza (size, *type):
#     print(f'Вы заказали такие пиццы с размером {size}: ')
#     for i in type:
#         print(f'-{i}')

# size=input('Размер: ')
# pizza(size, '4cheese')
# size=input('Размер: ')
# pizza(size, 'diablo','gavaiskaya','4meat','peperoni','ukranian')
# size=input('Размер: ')
# pizza(size, '4cheese', '4meat')
pizza=[]
while True:
    content = input('Enter ingridient: ')
    if content == 'quit':
        break
    elif content == 'ananas': #пасхалка
        print('I don\'t like ananas!') #ананас не добавляется в список ингредиентов
    else:
        pizza.append(content)
        content=''
print('Your ingridients:', ', '.join(pizza))