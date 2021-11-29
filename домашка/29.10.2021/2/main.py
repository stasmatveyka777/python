import funct
s=funct.animal("собака","Лорд")
print(s)

from funct import animal
b=animal("собака","Лорд")
print(b)

from funct import animal as a
c=a("собака","Лорд")
print(c)

import funct as f
d=f.animal("собака","Лорд")
print(d)

from funct import *
l=animal("собака","Лорд")
print(l)
