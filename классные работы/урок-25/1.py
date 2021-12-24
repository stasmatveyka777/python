import random
n=int(input("n= "))
a=[random.randint(0,10) for a in range(n)]
def n(x):
    if x%2==0:
        return True
    else:
        return False
t=list(filter(n, a))
print (t)
    
