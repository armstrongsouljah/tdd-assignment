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
        symbols = re.search('[@_!#$%^&*()<>?/\|}{~:]',password)

        if  lcase and ucase and number and symbols and len(password) >= 4:
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

    def register_user(self, name, **kwargs):
        """ creates a new account if one doesn't exist yet! """
        username = kwargs["username"]
        email = kwargs["email"]
        age  = kwargs["age"]
        password = kwargs["password"]
    
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
    
    def login(self, username, password):
        """ Checks suplied credentials against existing ones 
            returns True if both password and username are
            a match.
        """
        for account in self.accounts:
            name = account['name']
            if username and self.validate_username(username, name) == account['username'] and \
                self.validate_password(password) == account['password']:
                print("You're logged in")
                return True
            else:
                return False