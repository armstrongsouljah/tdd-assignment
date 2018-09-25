class Account:
    
    def __init__(self):
        self.accounts = []

    def register_user(self, name, username, age, email, password):
        self.account = dict(
            name=name,
            username=username,
            age=age,
            email=email,
            password=password
        )
        if len(self.account['password']) < 4:
            raise ValueError("Password should be atleast 4 characters and above")
        
        if not isinstance(self.account['age'], int) and self.account['age'] < 0:
            raise ValueError("Age must be a number and not equal to or less than 0")

        if self.account not in self.accounts:
            self.accounts.append(self.account)
