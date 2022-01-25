from user import User
class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(f'Привелегии: {self.privileges}')

class Admin(User, Privileges):
    def __init__(self, first_name, last_name, privileges, login_attempts=0, ):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = privileges
