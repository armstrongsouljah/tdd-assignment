import re

class Account:
    """ A class that handles creation of users and logging in 
        of registered users.    
    """
    
    def __init__(self):
        self.accounts = []

    def email_is_valid(self, email):
        if email and not re.findall(r'[\w\.-]+@[\w\.-]+', email):
            raise ValueError("Please enter a valid email address")
        else:
            return True

        if email =="" and email ==" ":
            raise ValueError("Email cant be empty")
        else:
            return True

    def validate_password(self, password):
        """ checks for password complexity """
        lcase = re.search(r"[a-z]", password)
        ucase = re.search(r"[A-Z]", password)
        number = re.search(r"[0-9]", password)

        if  lcase and ucase and number and len(password) >= 4:
            return True
        else:
            return False

    def validate_username(self, username, name):
        """ ensures that username is differen from name """

        if username and name and username != name\
             and len(username) >= 4:
            return True
        else:
            return False

    def validate_age(self, age):
        if isinstance(age, int) and age > 0:
            return True
        else:
            return False

    def register_user(self, name, username, email, age, password):
        """ creates a new account if one doesn't exist yet! """
    
        account = dict(
            name = name,
            username = self.validate_username(username, name),
            email = self.email_is_valid(email),
            age = self.validate_age(age),            
            password = self.validate_password(password)
        )

        if account not in self.accounts:
            self.accounts.append(account)
        else:
            print("User already exists")
            return False

        

    # def register_user(self, name, username, age, email, password, gender):
    #     self.account = dict(
    #         name=name,
    #         username=username,
    #         age=age,
    #         email=email,
    #         gender = gender,
    #         password=password
    #     )
    #     if len(self.account['password']) < 4:
    #         raise ValueError("Password should be atleast 4 characters and above")
            
        
    #     if self.account['gender'] != "female" and self.account['gender'] !="male":
    #         raise ValueError("Gender should be male / female!")
        
    #     if self.account['age'] <= 0:
    #         raise ValueError("Age must be above 0")

    #     if self.account['username'] == self.account['name']:
    #         raise ValueError("Username should be different from name")

    #     if self.account['username'] and len(self.account['username']) < 4:
    #         raise ValueError("Username should be atleast 4 characters and above")

    #     if self.account['email'] and not re.findall(r'[\w\.-]+@[\w\.-]+', self.account['email']):
    #         raise ValueError("Please enter a valid email address")

    #     if self.account['email'] =="" and self.account['email'] ==" ":
    #         raise ValueError("Email cant be empty")
     
    #     if self.account not in self.accounts:
    #         self.accounts.append(self.account)