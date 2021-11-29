#                                       8.6
def city_country(city,country):
   a= f' {city.title()}, {country.title()}'
   return a
i=0
while i<3:
   i+=1
   print("Если вы хотите закончить, напишите 'break'")
   city = input("Введите город: ")
   if city=="break": 
       break
   else:
       country=input("Введите страну: ")
       b=city_country(city,country)
       print(b)