class Human:
    def __init__(self,name,surname,age,place_of_bieth,year_of_bieth,now):
        self.name=name
        self.surname=surname
        self.age=age
        self.place_of_bieth=place_of_bieth
        self.year_of_bieth=year_of_bieth
        self.now=now
        print("\n Human creative")
    def info(self,first_year):
        print(f"\n name:{self.name}\n surname:{self.surname}\n age:{self.age}\n place_of_bieth:{self.place_of_bieth}\n year_of_bieth:{self.year_of_bieth}\n")
    def year_of_stud(self):
        years=self.now-self.first_year
p1=Human("Stas","Matveychuk",15,"UA",2006,)
p1.first_year=int(input("first year= "))
print(p1.first_year)
p1.info()
