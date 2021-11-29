import random
n = 3
m = 6
mat = [[random.randint(1,9) for i in range(m)] for i in range(n)]
print(mat)
print('--------------------')
for i in mat:
    print(f'\t\t{i}')