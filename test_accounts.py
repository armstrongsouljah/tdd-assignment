import unittest
from accounts import Account

class TestUserAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()
        self.email = "armstrongsouljah@gmail.com"
        self.password = "aDpho3nix!q"
        self.username = "armstrong"
        self.name = "soultech"
        self.age = 28

        self.sample_account = dict(
            username = self.username,            
            email = self.email,
            age = self.age,
            password = self.password
        )

    def test_isntantiation(self):
        self.assertIsInstance(self.account, Account)

    def test_email_should_be_valid(self):
        self.assertTrue(self.account.email_is_valid(self.email))

    def test_password_should_be_valid(self):
        self.assertTrue(self.account.validate_password(self.password))
        self.assertFalse(self.account.validate_password("23233232323232"))

    def test_username_should_be_valid(self):
        self.assertTrue(self.account.validate_username(self.username, self.name))

    def test_for_valid_age(self):
        self.assertTrue(self.account.validate_age(self.age))
        self.assertFalse(self.account.validate_age(0))

    def test_user_can_register(self):
        self.assertEqual(len(self.account.accounts), 0)
        self.account.register_user(self.name, **self.sample_account)
        self.assertEqual(len(self.account.accounts), 1)

    def test_duplicate_users(self):
        self.account.register_user(self.name, **self.sample_account)
        self.assertFalse(self.account.register_user(self.name, **self.sample_account))

    def test_user_can_login(self):
        self.account.register_user(self.name, **self.sample_account)
        self.assertTrue(self.account.login(self.username, self.password))
        self.assertFalse(self.account.login("armstron", "phoder"))
