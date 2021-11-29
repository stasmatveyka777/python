n=int(input('Введите n:   '))
s=0
d=1
for i in range(1,n+1):
	s = s+i
print(s)
s=0
while d <=n:
	s = s +d
	d+=1
print(s)