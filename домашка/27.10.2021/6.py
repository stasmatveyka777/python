#                                           8.12
def sandwich(a,b):
    b+=a
    return b
s=""
b=""
x=" "
while True:
    a=str(input("Введите компонент вашего сэндвича (Если вы закончили, напишите 'Ready'): "))
    if a=="Ready":
        break
    else:
        s+=sandwich(a,b)+x

print(s)