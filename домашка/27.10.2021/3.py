#                                       8.5
def describe_city(city,country):
   a=f'{city.title()} is in {country.title()}'
   return a
i=0
while i<3:
   i+=1
   print("Если вы хотите закончить, напишите 'break'")
   city = input("Введите город: ")
   if city =="Kiev" or city =="Dnepr":
       country = 'Ukraine'
   elif city=="break":
       break
   else:
       country=input("Введите страну: ")
   b=describe_city(city,country)
   print(b)