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
            name = self.name,
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

    def test_username_should_be_valid(self):
        self.assertTrue(self.account.validate_username(self.username, self.name))

    def test_for_valid_age(self):
        self.assertTrue(self.account.validate_age(self.age))

    def test_user_can_register(self):
        self.assertEqual(len(self.account.accounts), 0)
        self.account.register_user(**self.sample_account)
        self.assertEqual(len(self.account.accounts), 1)

    def test_duplicate_users(self):
        self.account.register_user(**self.sample_account)
        self.assertFalse(self.account.register_user(**self.sample_account))
