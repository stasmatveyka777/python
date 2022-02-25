password = input("введите пароль: ")
print("Введите пароль повторно")
password2 = input("введите пароль 2 раз: ")
if password2 == password:
    print("OK")
else:
    print("не верно!")
