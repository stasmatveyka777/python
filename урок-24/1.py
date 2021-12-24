def gen():
    print("Loading start")
def gen1():
    n=0
    while n<100:
        print("Loading ...")
        n+=5
        r = f"{n}%"
        yield r
t=gen1()
for i in gen1():
    print(i)
def gen2():
    print("Loading end")
