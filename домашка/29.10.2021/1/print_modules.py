import printing_functions
s=" "
while True:
    a=input("Что напечатать(чтобы выйти напишите quit): ")
    if a=="quit":
        break
    else:
        s+=printing_functions.print_modules(a)
print(f'Ваш заказ:"{s}"')
