
#7.4,7.6
active=True
while active:
    d=input("Какуе добавление вы желаете для вашей пиццы?(Для отмены напишите 'quite'")
    if d=="quite":
        print("Ваша пицца готовиться")
        active= False
    else:
        print(f"{d} Добавлена в вашу пиццу")
