from admin import Privileges, Admin
from user import User
user1 = User('Стас','Матвейчук')
user1.describe_user()
user1.greeting_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

admin1 = Admin('Admin', 'admin', 'Allowed to add message, Allowed to delete user, Allowed to ban users')
priv=Admin('Admin', 'admin', 'Allowed to add message, Allowed to delete user, Allowed to ban users')
priv.show_privileges()
