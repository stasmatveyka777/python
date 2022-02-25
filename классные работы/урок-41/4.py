score = int(input("Введите вашу оценку: "))

if score >= 12:
    print("Без лишних слов ты отличник")
elif score >= 10:
    print("Ты красава")
elif score >= 8:
    print(" ам надо постораться")
elif score >= 6:
    print("Ну это у тебя стабильно")
elif score >= 4:
    print("да ты реально плох")
elif score >= 2:
    print("иди учи уроки двоешник")   
else:
    print("Вы не сдали экзамен")
