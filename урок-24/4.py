def gen_n(i):
    if i%2==0:
        return True
    else:
        return False
a=[i for i in range(1098789781)]
f=list(filter(gen_n,a))
print(f)

