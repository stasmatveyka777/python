import random
n=int(input('n='))
m=int(input('m='))
mat=[[random.randint(0,9) for j in range(m) ] for i in range(n)]
for f in mat:
    print(f' {f}')
diagonal=[mat[i][j] for i in range(n) for j in range(m) if i==j]
print(diagonal)
k=int(input("k="))
str_mat=[mat[k-1][j] for j in range(m)]
print(str_mat)
