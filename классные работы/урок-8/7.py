n = int(input('Введите число:   '))
i = 1
s = 1/2
b= 0
while i <=n:
	b+=s
	s/=2
	i+=1
print(b)