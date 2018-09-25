import unittest
from accounts import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()