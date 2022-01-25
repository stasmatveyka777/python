class User():
    def __init__(self,first_name,last_name,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f'{str(self.first_name).title()} {str(self.last_name).title()}')
    def greeting_user(self): # Приветствие
        print(f'Hello, {str(self.first_name).title()} {str(self.last_name).title()}')
    def increment_login_attempts(self): # Увеличивает login_attempts на 1 
        self.login_attempts+=1
    def reset_login_attempts(self): # Обнуляет login_attempts
        self.login_attempts = 0