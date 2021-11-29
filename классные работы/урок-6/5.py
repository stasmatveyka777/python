import random
for i in range(10):
    
    summ=0
    cort = {random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10)}
    print(cort)
    for i in cort:
        if i>=5 and i<=10:
          summ=summ+i
    print(summ)
