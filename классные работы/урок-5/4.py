a = float(input('Введите первое число   '))
b = float(input('Введите второе число   '))
if a < b:
    a = 0
    b = 1
else:
    b = 0
    a = 1
print(f'Первое число: {a}, а второе: {b}')

al = ['1','2','3','4']
i = 0
while i < 3:
    pp = i
    oo = i
    print('del_pp',pp,f'al.pop({oo})')
    
