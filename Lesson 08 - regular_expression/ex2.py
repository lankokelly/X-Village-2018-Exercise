import re
class AuthSystem:
    
    def __init__(self):
        self.username_regex = re.compile(r'(?P<name>[A-Z][a-z][a-z])')
        self.password_regex = re.compile(r'(?P<pass>[a-z][a-z][a-z][0]\d\d\d\d\d)')
    
    def check_username(self, username):
        if(len(username)!=3):
            print("Username format error! Your username is",username)
            return False
        if self.username_regex.search(username) is not None:
            return True
        else: 
            print("Username format error! Your username is", username)
            return False

    def check_password(self, password):
        if(len(password)!=9):
            print("Password legnth error! Your password length is", len(password))
            return False
        if self.password_regex.search(password) is not None:
            return True
        else:
            print("Password format error! Your password is", password)
            return False
        
    def checkboth(self, username, password):
        if not self.check_username(username):
            return
        if not self.check_password(password):
            return
        print("Welcome,",username)

auth = AuthSystem()
for i in range (1,5):
    username = input('Username is : ')
    password = input('Password is : ')
    auth.checkboth(username,password)