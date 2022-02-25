x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    print('первая четверть')
elif x<0 and y>0:
    print('вторая четверть')
elif x<0 and y<0:
    print('третья четверть')
elif x>0 and y<0:
    print('четвёртая четверть')
else:
    print("Error!")
