list_1=[4,16,64,256]
list_gen=(i**(1/2) for i in list_1)

while list_gen:
    print(next(list_gen))

