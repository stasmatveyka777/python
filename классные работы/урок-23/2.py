def gen(n):
    print("Первый перебор")
    yield n
    print("Второй перебор")    
    yield n+1
    print("3 перебор")
    yield n*3
n=int(input("n="))
t=gen(n)
#print(next(t))
#print(next(t))
#print(next(t))
for i in t:
    print(i)
