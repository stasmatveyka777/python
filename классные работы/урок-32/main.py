#                                   9.1
print(9.1)
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name.title()}' have {self.cuisine_type} cuisine")
    def open_restaurant(self):
        print("Restaurant open!")
r1=Restaurant("restaurant","ukrainian")
print(r1.restaurant_name)
print(r1.cuisine_type)
r1.describe_restaurant()
r1.open_restaurant()
#                                   9.2
print("")
print(9.2)
r2=Restaurant("Vilen","french")
r2.describe_restaurant()
r3=Restaurant("Catering","english")
r3.describe_restaurant()
r4=Restaurant("Amalfi","chinese")
r4.describe_restaurant()
#                                   9.3
print("")
print(9.3)
class User:
    def __init__(self,first_name,last_name,age,place,date_of_registration):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.place=place
        self.date_of_registration=date_of_registration
    def describe_user(self):
        print(f" Name:{self.first_name}\n Surname:{self.last_name}\n Age:{self.age}\n Place:{self.place}\n Date:{self.date_of_registration}")
    def greet_user(self):
        print(f"Hi,{self.first_name} {self.last_name}!")
u1=User("Tima","Pylypenko",16,"Ukraine",2015)
u1.describe_user()
u1.greet_user()
u2=User("Ilya","Yushenko",14,"Spanish",2020)
u2.describe_user()
u2.greet_user()
u3=User("Kim","Tyn",17,"Chine",2005)
u3.describe_user()
u3.greet_user()
#                                   Rectangle
print("")
print("Rectangle")
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def square(self):
        print(f"Площа:{self.length*self.width}")
length=float(input("Введіть довжину:"))
width=float(input("Введіть ширину:"))
r1=Rectangle(length,width)
r1.square()
#                                       9.4
print("")
print("9.4")
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name.title()}' have {self.cuisine_type} cuisine")
    def open_restaurant(self):
        print("Restaurant open!")
    def set_number_served(self,new_number_served):
        self.number_served=new_number_served
        return self.number_served
    def increment_number_served(self,time):
        print(self.number_served+(10*time))
r1=Restaurant("restaurant","ukrainian")
print(r1.number_served)
r1.number_served=12
print(r1.number_served)
number_served=int(input("Сколько людей вы обслужили?:"))
r1.set_number_served(number_served)
print(r1.number_served)
while True:
    time=float(input("За сколько часов вас интерисует количество?:"))
    if time<=0:
        print("Неверно указано время")
    else:
        break
r1.increment_number_served(time)
#                                           9.5
print("")
print(9.5)
class User:
    def __init__(self,first_name,last_name,age,place,date_of_registration,login_attempts=0):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.place=place
        self.date_of_registration=date_of_registration
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f" Name:{self.first_name}\n Surname:{self.last_name}\n Age:{self.age}\n Place:{self.place}\n Date:{self.date_of_registration}")
    def greet_user(self):
        print(f"Hi,{self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts=self.login_attempts+1
        return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts
u1=User("Tima","Pylypenko",16,"Ukraine",2015)
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(u1.login_attempts)
u1.reset_login_attempts()
print(u1.login_attempts)
#                                           9.6
print("")
print(9.6)
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        Restaurant.__init__(self,restaurant_name,cuisine_type)
        self.flavors=flavors
    def describe_flavors(self):
        for i in self.flavors:
            print(i)
r1=IceCreamStand("restaurant","ukrainian",["Milk","Chocolate","Fruit"])
r1.describe_flavors()
#                                           9.7
print("")
print(9.7)
class Admin(User):
    def __init__(self,first_name,last_name,age,place,date_of_registration,privileges):
        User.__init__(self,first_name,last_name,age,place,date_of_registration)
        self.privileges=privileges
    def show_privileges(self):
        for i in self.privileges:
            print(f"You can {i}")
u1=Admin("Tima","Pylypenko",16,"Ukraine",2015,["ban other users","kick other users","mute other users"])
u1.show_privileges()
#                                           9.8
print("")
print(9.8)
class Admin(User):
    def __init__(self,first_name,last_name,age,place,date_of_registration,privileges):
        User.__init__(self,first_name,last_name,age,place,date_of_registration)
        self.privileges=privileges
    def show_privileges(self):
        for i in self.privileges:
            print(f"You can {i}")

a1=Admin("Tima","Pylypenko",16,"Ukraine",2015,["Allowed to add","Allowed to delete users","Allowed to ban users"])

class Privileges:
    def __init__(self,privileges=a1.privileges):
        self.privileges=privileges
    def show_privileges(self):
        Admin.show_privileges(self)
priv=Privileges()
class Admin(User):
    def __init__(self,first_name,last_name,age,place,date_of_registration,privileges=priv.privileges):
        User.__init__(self,first_name,last_name,age,place,date_of_registration)
        self.privileges=privileges
    def show_privileges(self):
        for i in self.privileges:
            print(f"You can {i}")

u2=Admin("Tima","Pylypenko",16,"Ukraine",2015)
u2.show_privileges()
#                                       9.10
from Restaurant import *
print("")
print("9.10")

r1=Restaurant("Comfi","electronical")
r1.describe_restaurant()
#                                       9.11
print("")
print("9.11")
from User_Admin_Privileges import *
u1=Admin("Tima","Pylypenko",16,"Ukraine",2015)
u1.show_privileges()
#                                       9.12
print("")
print("9.12")
from User import *
from Admin_and_Privileges import *
a1=Admin("Tima","Pylypenko",16,"Ukraine",2015,["Allowed to add","Allowed to delete users","Allowed to ban users"])
a1.show_privileges()
