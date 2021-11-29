def month (m, season):
    for i, j in month_seasons.items():
        if m in i:
            season = j
        elif m>12 and m<1:
            print (error)
    return season

month_seasons = {
    (12, 1, 2): 'Zima',
    (3, 4, 5): 'Vesna',
    (6, 7, 8): 'Leto',
    (9, 10, 11): 'Osen'
}
error = f"Error!"
m = int(input('Enter number of your month: '))
a=month(m, error)
print(a)