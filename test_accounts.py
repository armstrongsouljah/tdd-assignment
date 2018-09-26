import unittest
from accounts import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()
        self.accounts = self.account.accounts
        self.sample_account = dict(
            name = "armstrong",
            username = "soultech",
            age = 24,
            email = "armstrongsouljah@gmail.com",
            password = "Aa9s0!*",
            gender = "male"
        )

        self.sample_account2 = dict(
            name = "soultech",
            username = "soultech",
            age = 24,
            email = "armstrongsouljah@gmail.com",
            password = "Aa9s0!*",
            gender = "male"
        )

        self.sample_account3 = dict(
            name = "pauljonas",
            username = "kyx",
            age = 24,
            email = "armstrongsouljah@gmail.com",
            password = "Aa9s0!*",
            gender = "male"
        )

        self.sample_account4 = dict(
            name = "pauljonas",
            username = "kyxdededed",
            age = 0,
            email = "armstrongsouljah@gmail.com",
            password = "Aa9s0!*",
            gender = "male"
        )

        self.sample_account5 = dict(
            name = "pauljonas",
            username = "kyx",
            age = 35,
            email = "armstrongsouljahgmail.com",
            password = "Aa9s0!*",
            gender = "male"
        )

        self.sample_account6 = dict(
            name = "pauljonas",
            username = "kyxdeded",
            age = 34,
            email = " ",
            password = "Aa9s0!*",
            gender = "male"
        )

        self.sample_account7 = dict(
            name = "pauljonas",
            username = "kyxdeded",
            age = 23,
            email = "23232323232322323",
            password = "Aa9s0!*",
            gender = "male"
        )

    def test_user_can_register(self):
        self.assertEqual(len(self.accounts), 0)
        self.account.register_user(**self.sample_account)
        self.assertEqual(len(self.accounts), 1)

    def test_username_not_similar_to_name(self):
        with self.assertRaises(ValueError) as context:
            self.account.register_user(**self.sample_account2)
            self.assertTrue("Username should be different from name" in context.exception)

    def test_username_not_below_4_characters(self):
        with self.assertRaises(ValueError) as context:
            self.account.register_user(**self.sample_account3)
            self.assertTrue("Username should be atleast 4 characters and above" in context.exception)

    def test_age_should_be_number(self):
        with self.assertRaises(ValueError) as E:
            self.account.register_user(**self.sample_account4)
            self.assertTrue("Age must be above 0" in E.exception)

    def test_email_should_be_valid(self):
        with self.assertRaises(ValueError) as context:
            self.account.register_user(**self.sample_account5)
            self.assertTrue("Please email address" in context.exception)
    
    def test_email_should_not_be_empty(self):
        with self.assertRaises(ValueError) as context:
            self.account.register_user(**self.sample_account6)
            self.assertTrue("Email cant be empty" in context.exception)

        