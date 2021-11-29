#7.5
age=int(input("Введите ваш возраст"))
if age<3:
    print("Билет бесплатный")
elif age>=3 and age<=12:
    print("Билет стоит 10$")
else:
    print("Билет стоит 15$")
