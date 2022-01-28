class Animal():
    def __init__(self,species,animal_sound):
        self.species = species
        self.animal_sound = animal_sound
    def info(self):
        print(f'{self.species}')
    def sound(self):
        print(f'{self.animal_sound}')
class Dog(Animal):
    def __init__(self, species, animal_sound):
        super().__init__(species, animal_sound)
class Cat(Animal):
    def __init__(self, species, animal_sound):
        super().__init__(species, animal_sound)  
def show_animal_info(name,spec,sound):
    name = Animal(spec,sound)
    name.info()
    name.sound()
def show_animal_info_dog(name,spec,sound):
    name = Dog(spec,sound)
    name.info()
    name.sound()
def show_animal_info_cat(name,spec,sound):
    name = Cat(spec,sound)
    name.info()
    name.sound()
show_animal_info('ordinary animal','I`m an - ordinary animal','Grrr!')
show_animal_info_dog('dog','I`m an - dog','Woof! Woof!')
show_animal_info('cat','I`m an - cat','Meow!')
book = Animal('book','scr')
print(f'{book.species} not an animal')

