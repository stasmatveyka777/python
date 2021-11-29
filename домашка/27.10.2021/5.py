                                        #   8.7;8.8
def make_album(name_s,name_a,signs):
   if signs==None:
       a = f'{name_s.title()} \n{name_a.title()}'
   else:
       a = f'{name_s.title()} \n{name_a.title()} \n{signs} signs'
   return a
i=0
while i<3:
   i+=1
   print("Если вы хотите закончить, напишите 'break'")
   name_s=str(input("Введите имя исполнителя: "))
   if name_s=="break":
       break
   name_a=str(input("Введите название альбома: "))
   signs=str(input("Введите количество дороже(Если не известно, нажмите 'Enter'"))
   if signs =="":
       signs=None
   b=make_album(name_s,name_a,signs)
   print(b)