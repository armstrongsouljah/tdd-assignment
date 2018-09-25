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
            password = "Aa9s0!*"
        )

    def test_user_can_reigster(self):
        self.assertEqual(len(self.accounts), 0)
        self.account.register_user(**self.sample_account)
        self.assertEqual(len(self.accounts), 1)