def den (x):
    x*=2
    yield x
t=den(5)
print(t)
print(next(t))
