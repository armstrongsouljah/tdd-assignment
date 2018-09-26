import re

class Account:
    """ A class that handles creation of users and logging in 
        of registered users.
    
    """
    
    def __init__(self):
        self.accounts = []
        self.gender = "male"

    def change_gender(self,_gender):
        self.gender = _gender
        return self.gender
        

    def register_user(self, name, username, age, email, password, gender):
        self.account = dict(
            name=name,
            username=username,
            age=age,
            email=email,
            gender = gender,
            password=password
        )
        if len(self.account['password']) < 4:
            raise ValueError("Password should be atleast 4 characters and above")
            
        
        if self.account['gender'] != "female" and self.account['gender'] !="male":
            raise ValueError("Gender should be male / female!")
        
        if self.account['age'] <= 0:
            raise ValueError("Age must be above 0")

        if self.account['username'] == self.account['name']:
            raise ValueError("Username should be different from name")

        if self.account['username'] and len(self.account['username']) < 4:
            raise ValueError("Username should be atleast 4 characters and above")

        if self.account['email'] and not re.findall(r'[\w\.-]+@[\w\.-]+', self.account['email']):
            raise ValueError("Please enter a valid email address")

        if self.account['email'] =="" and self.account['email'] ==" ":
            raise ValueError("Email cant be empty")
     
        if self.account not in self.accounts:
            self.accounts.append(self.account)