a = [1,2,3]
b = [4,5,6,7]
c = [(i,g) for i in a for g in b]
for f in c:
    print(f)