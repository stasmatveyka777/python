class Car():
    def __init__(self,marka,model,year,adomiter):
        adomiter = 0
        self.marka = marka
        self.model = model
        self.year = year
        self.adomiter = adomiter
    def get_discript_name(self):
        print(f'\n\nМарка машини: {self.marka}\nМодель: {self.model}\nГод: {self.year}')
    def read_adomiter(self):
        print(f'Изначальный адометр:{self.adomiter}')    
    def appdate(self,adomiter_value):
        print(f'Адометр: {adomiter_value}')
        if probeg > self.adomiter:
            # print(f'Скручивать нельзя!')
            self.adomiter = adomiter_value
        else:
            print('Нельзя скручивать')
        
            
    def probeg_adomint(self,myprobeg):
        self.adomiter+=myprobeg
        print(f'После использование пробег становит: {self.adomiter}')
class Electrocar(Car):
    def __init__(self, marka, model, year, adomiter, battery):
        super().__init__(marka, model, year, adomiter)
        self.battarey = battery
        print(f'Вы купили {self.marka} {self.model} {self.year} года C {self.adomiter} пробегом. Батарея : {self.battarey}мА·ч')
my_new_car= Car('BMW','M3',2016,0)
my_new_car.adomiter = 23
probeg= int(input('Введите probeg ====>   '))
my_new_car.get_discript_name()
my_new_car.read_adomiter()
my_new_car.appdate(probeg)
my_new_car.probeg_adomint(probeg)

your_new_car = Electrocar('Tesla','Model 3',2018, 0, 3140)

    