class Pyhton:
    def info(self,n):
        for i in range(n):
            print(f"\n name:{self.name}\n surname:{self.surname}\n age:{self.age}\n place_of_bieth:{self.place_of_bieth}\n")
    def year(self, year_new):
        return year_new-self
                            
    pass
p1=Pyhton()
p1.name="Stas"
p1.surname="Matveychuk"
p1.age="15"
p1.place_of_bieth="UA"
p1.year_of_bieth=2006
p1.info()

p2= Pyhton()
p2.name="Yarik"
p2.surname="Vigovskiy"
p2.age="14"
p2.place_of_bieth="UA"
p2.year_of_bieth=2007
p2.info()
p2.year()

p3= Pyhton()
p3.name="Illa"
p3.surname="Katerinich"
p3.age="14"
p3.place_of_bieth="UA"
p3.year_of_bieth=2007
p3.info()
p3.year()
