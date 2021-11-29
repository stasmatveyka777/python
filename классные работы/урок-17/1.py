a = [i for i in range(1, 11)]
print(a)
a = [i for i in range(1, 11) if i>=7]
print(a)
a = [i if i>=4 else "false" for i in range(1, 11) ]
print(a)
a = ["true_2" if i%2==0 else "true_3" if i%3==0 else "false"  for i in range(1, 11) ]
print(a)