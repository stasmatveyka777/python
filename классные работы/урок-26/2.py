class Machine:
    def __init__(self,mark,name,time,speed):
        self.mark=mark
        self.name=name
        self.time=time
        self.speed=speed
class Rocket(Machine):
    def info_1(self):
        print(f"\n mark:{self.mark}\n name:{self.name}\n time:{self.time}\n speed:{self.speed}\n")
class Car(Machine):
    def info_2(self):
        print(f"\n mark:{self.mark}\n name:{self.name}\n time:{self.time}\n speed:{self.speed}\n")
p2=Car("BAZ","2110","324 sec",2100)
p2.info_2()
while True:
    n=int(input("Введите 1 или 2 или 3 что по душе будет= "))
    if n==1:
        
