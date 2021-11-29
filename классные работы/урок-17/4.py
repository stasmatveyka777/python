# c = {i:i**2 for i in range(20)}
# for k,v in c.items():
#      print(k,v)
c = {i:i**2 for i in range(20) if i>=5}
m = {g:l for g,l in c.items() if l<=100}
for k,v in m.items():
     print(k,v)