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
        self.login_attempts+=1
        return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts
