myname = input('Введите ваше имя ===>  ')
nearname = input('Введите имя соседа по парте ===>  ')
def pr(a,b):
	print(f'Ваше имя - {a.title()}.\nИмя соседа по парте - {b.title()}')
pr(myname,nearname)