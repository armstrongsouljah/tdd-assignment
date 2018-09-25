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
        return 
