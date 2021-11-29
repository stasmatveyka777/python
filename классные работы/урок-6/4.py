
T=[2.3, 4.5, 3.5, 10.3, 5]
b=T[0]
for i in T:
    if i > b:
        b = i
print(f'Через цикл: {b}')
