x1 = int(input('x='))
if x1>0:
    y1=2*x1-10
elif x1==0:
    y1=0
elif x1<0:
    y1=2*abs(x1)-1
else:
    print(False)
print(f'y={y1}')
