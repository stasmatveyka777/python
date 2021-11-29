def month (m):
    for i, j in month_seasons.items():
        if m in i:
            season = j
        elif m>12 or m<1:
            season = f"Error!"
    return season

month_seasons = {
    (12, 1, 2): 'Zima',
    (3, 4, 5): 'Vesna',
    (6, 7, 8): 'Leto',
    (9, 10, 11): 'Osen'
}
while True:
    m = str(input('Enter number of your month: '))
    if m == 'break':
        break
    else:
        m=int(m)
        a=month(m)
        print(a)

num = [1, 2, 3, 4, 5]
num2 = [a**2 for a in num if a>2]
print(num2)