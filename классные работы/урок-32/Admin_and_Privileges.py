from User import *
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
