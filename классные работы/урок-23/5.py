def gen(n):
    a,b=1,1
    for i in range(n):
        yield a
        a,b=b,a+b
n=int(input("n="))
t=gen(n)
for i in t:
      print(i)
