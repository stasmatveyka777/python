class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        print(f'Person created')
    def info(self):
        print(f'{self.name} says hello')

class Student(Human):
    def __init__(self, name, age,place_of_studying):
        super().__init__(name, age)
        self.place_of_studying = place_of_studying
    def studying(self):
        print(f'{self.place_of_studying}')
    def study(self):
        print(f'Student {self.name} - studies')
    def info(self):
        print(f'Student created \n\t\tname : {self.name}\n\t\tage: {self.age}')
# class Teacher(Human):
#     def teach(self):
#         print(f'{self.name} - teacher')
s1 = Student('Roma',16,'KPL')
s1.info()
s1.studying()
s1.study()
# s1.study()
# t1 = Teacher('Nico',45)

