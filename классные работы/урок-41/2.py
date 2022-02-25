i = 0
your_password = input('Введите пароль  ')
while i <3:  
    check_password= input('Введите пароль еще раз  ')
    if your_password != check_password:
        i+=1
        print("Ошибка не верный пароль")
    else: 
        print('Успешно вы зашли в свой кабинет')
        break
else:
    print('Извините ошибка')
