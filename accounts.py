class Account:
    
    def __init__(self):
        self.accounts = []

    def register_user(self, name, username, age, email, password, gender):
        self.account = dict(
            name=name,
            username=username,
            age=age,
            email=email,
            password=password,
            gender=gender
        )
        if len(self.account['password']) < 4:
            raise ValueError("Password should be atleast 4 characters and above")
        
        if self.account['gender'] != "female" and self.account['gender'] !="male":
            raise ValueError("Gender should be male / female!")
        
        if not isinstance(self.account['age'], int) and self.account['age'] <= 0:
            raise ValueError("Age must be a number and not equal to or less than 0")

        if self.account['username'] == self.account['name']:
            raise ValueError("Username should be different from name")

        if self.account['username'] and len(self.account['username']) < 4:
            raise ValueError("Username should be atleast 4 characters and above")


        

        if self.account not in self.accounts:
            self.accounts.append(self.account)
