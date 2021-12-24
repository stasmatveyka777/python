class Pyhton:
    def __init__(self, name,surname,age,place_of_bieth,year_of_bieth):
        self.name=name
        self.surname=surname
        self.age=age
        self.place_of_bieth=place_of_bieth
        self.year_of_bieth=year_of_bieth

    def info(self):
        print(f"\n name:{self.name}\n surname:{self.surname}\n age:{self.age}\n place_of_bieth:{self.place_of_bieth}\n year_of_bieth:{self.year_of_bieth}\n")    
    
p1=Pyhton("Den","Dmitriev",24,"UA",1997)
p1.info()
p2=Pyhton("Stas","Matveychuk",15,"UA",2006)
p2.info()
p3=Pyhton("Illa","Katerinich",14,"UA",2007)
p3.info()
