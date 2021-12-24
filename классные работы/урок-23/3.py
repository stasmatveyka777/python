language=["python","C++","PHP"]
def gen(i,a):
    for i in a:
        yield i
i=0
t=gen(i,language)
for m in t:
    print(m)
