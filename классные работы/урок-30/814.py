from multiprocessing.spawn import prepare


username= input('Введите username ====>   ')
password= input('Введите password ====>   ')
class Bank():
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):
        while True:
            logname= input('Введите log-name ====>   ')
            logpass= input('Введите log-pass ====>   ')
            if logname ==self.name and logpass==self.password:
                break
            else: print(f'ERROR')
                
    def start_bank(self):
        print(f'Hello, {self.name}! I open a bank account')
    def balance(self,balance):
        self.balance = balance
        print(f'Your balance: {balance} c.u.')
    def add_balance(self,dep_balance):
        self.balance= self.balance+ dep_balance
        print(f'You depostie {dep_balance} c.u. Now your balance: {self.balance} c.u.')
    def remove_balance(self,rem_balance):
        
        if self.balance < rem_balance:
            print(f'ERROR!!  Not enough money! In your acc {self.balance} c.u.')
        else:
            self.balance= self.balance - rem_balance
            print(f'You took away {rem_balance} c.u. Now your balance: {self.balance} c.u.')

user1 = Bank(username,password)
user1.login()
user1.start_bank()
user1.balance(0)
user1.add_balance(200)
user1.add_balance(500)
user1.remove_balance(600)
user1.remove_balance(200)