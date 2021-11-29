import random
import os
aaa = 0

while aaa == 0:
	os.system('cls||clear')
	task = int(input('Выбери номер задачи(4-10)' + '\n'))
	if (task == 4):
		family = ['давид','илья','максим']
		i = 0
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1

		aaa = aaa + 1
	elif(task == 5):
		family = ['давид','илья','максим']
		i = 0
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1

		ir = random.randint(0,2)
		print('\nК сожелению ', family[ir].title(), ' не сможет прийти, поэтому я составил другой список\n')
		i = 0
		family[ir] = 'богдан'
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1
		aaa = aaa + 1
	elif(task == 6):
		family = ['давид','илья','максим']
		i = 0
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1

		ir = random.randint(0,2)
		print('\nК сожелению ', family[ir].title(), ' не сможет прийти, поэтому я составил другой список\n')
		i = 0
		family[ir] = 'богдан'
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1
		print('\nТак-как я купил новый стол я приглашу еще больше гостей. И так вот мой новый список: \n')
		family.insert(0,'тимофей')
		family.insert(2,'дима')
		family.append('юля')
		i = 0
		while i <= 5:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1
		aaa = aaa + 1
	elif(task == 7):
		family = ['давид','илья','максим']
		i = 0
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1

		ir = random.randint(0,2)
		print('\nК сожелению ', family[ir].title(), ' не сможет прийти, поэтому я составил другой список\n')
		i = 0
		family[ir] = 'богдан'
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1
		print('\nТак-как я купил новый стол я приглашу еще больше гостей. И так вот мой новый список: \n')
		family.insert(0,'тимофей')
		family.insert(2,'дима')
		family.append('юля')
		i = 0
		while i <= 5:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1

		print('\nЯ обнаружил что нового стола хватит только на двух гостей, поэтому вот мой новый список:\n')
		p1 = random.randint(0,5)
		p2 = random.randint(0,4)
		p3 = random.randint(0,3)
		p4 = random.randint(0,2)
		del_fam1 = family.pop(p1)
		del_fam2 = family.pop(p2)
		del_fam3 = family.pop(p3)
		del_fam4 = family.pop(p4)
		
		print('Привет, ',family[0].title()+ '. Ранние приглашение на мой день рождения все еще действительно.')
		print('Привет, ',family[1].title()+ '. Ранние приглашение на мой день рождения все еще действительно.')

		del family[1]
		del family[0]

		print('Список после всех изменений:         ',family)
		aaa = aaa + 1
	elif( task == 8):
		stran = ['France','Spain','Brazil','Portugal','Canada']
		stran_abc = sorted(stran)
		stran_cba = sorted(stran, reverse = True)
		print(stran)
		print(stran_abc)
		print(stran)
		print(stran_cba)
		aaa = aaa + 1
	elif( task == 9):
		family = ['давид','илья','максим']
		i = 0
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1

		ir = random.randint(0,2)
		print('\nК сожелению ', family[ir].title(), ' не сможет прийти, поэтому я составил другой список\n')
		i = 0
		family[ir] = 'богдан'
		while i <= 2:
			print('Приглашаю тебя, ',family[i].title(),' на мой день рождения!')
			i = i + 1
		print('Всего приглашенных:  ',len(family))
		aaa = aaa + 1
	elif(task == 10):
		print('Мой список будет необычным. Я затрону тему киберспорта в CS:GO')
		top = ['Natus Vincere','Gambit','Vitality','G2','Heroic']
		i = 0
		while i <=4:
			n = i + 1
			print('Команда номер',n, 'во всем мире:   ', top[i])
			i = i + 1
		print('Совсем недавно команда FaZe обогнала Heroic и поэтому вот новый список:')
		top[4] = 'Faze'
		i = 0
		while i <=4:
			n = i + 1
			print('Команда номер',n, 'во всем мире:   ', top[i])
			i = i + 1
		print('А вот команды из СНГ')
		del_top1 = top.pop(4)
		del_top2 = top.pop(3)
		del_top3 = top.pop(2)
		i = 0
		while i <= 1:
			print('Команда ',top[i])
			i = i + 1
		top.append(del_top1)
		top.append(del_top2)
		top.append(del_top3)
		print('Команды в алфовитном порядке:\n' , sorted(top), '\nКоманды в обратном порядке:\n',sorted(top, reverse = True) )
		aaa = aaa + 1
	else:
		print('ERROR')








