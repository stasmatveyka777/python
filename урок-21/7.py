list=[11,5,8,3215,5,3,20,123,21,4,525,9,20]
s=0
for i in list:
    if i<30 and i%3==0:
        print(i)
    else:
        s+=i
print(s)
