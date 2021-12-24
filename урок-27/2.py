class Machine:
    def __init__(self,name,mark,time,speed,user):
        self.name=name
        self.mark=mark
        self.time=time
        self.speed=speed
        self.user=user
        print("Machine detected")
        
class Car(Machine):
    def info_c(self):
        print(f"Car:\n\t Mark:{self.mark}\n\t Name:{self.name}\n\t Time:{self.time}\n\t Speed:{self.speed}")
    def info_user1(self):
        print(f"User:{self.user},Speed:{self.speed},Time:{self.time}")
class Rocket(Machine):
    def info_r(self):
        print(f"Rocket:\n\t Mark:{self.mark}\n\t Name:{self.name}\n\t Time:{self.time}\n\t Speed:{self.speed}")
    def info_user2(self):
        print(f"User:{self.user},Speed:{self.speed},Time:{self.time}")
while True:
    n=int(input("Если хотите полететь в космос введите 1, 2-если хотите на Кубу"))
    if n==1:
        f=Rocket("Nasa","SpaceX","2 years",12,"Ilya")
        f.info_r()
        f.info_user2()
    elif n==2:
        f=Car("Lamborghini Murciélago","Lamborgini","24 hours",2,"Tima")
        f.info_c()
        f.info_user1()
    else:
        print("Try again")
