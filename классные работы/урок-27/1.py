class Human:
    year=2021
    def __init__(self,name,surname,age,place_of_birth,first_year):
        self.name=name
        self.surname=surname
        self.age=age
        self.place_of_birth=place_of_birth
        self.first_year=first_year
        #self.now=now
        print("Human created")
    def info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nSurname:{self.surname}\nStudy in KPL\nFrom:{self.place_of_birth}")
    def year_of_studying(self):
        return self.year-self.first_year #Human.year
I=Human("Ilya","Yushenko",16,"UA",2015)
I.info()
print(I.year_of_studying())
