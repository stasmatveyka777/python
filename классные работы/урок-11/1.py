def fullname(name,surname):
    a = f'{name.title()} {surname.title()}'
    return a
while True:
    print('Укажите имя и фамилию')
    name = input('Имя ===>   ')
    if name == 'break':break
    surname = input('Фамилия ===>   ')
    b = fullname(name,surname)
    print(b)