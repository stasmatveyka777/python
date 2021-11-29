money = int(input('Введите депозит    '))
percent = float(input('Введите %    '))
year = 5
for i in range(year):
    money = money + money*percent/100
    print(money)
    i+=1

