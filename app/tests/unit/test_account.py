from django.test import TestCase
import django.utils.timezone as timezone
import datetime
from app.models import Account


class AccountTest(TestCase):
    def test_confirm_transfer(self):
        receiver = Account.objects.get(number='qwe123rty098d')
        print(receiver.number)
        old_amount = receiver.current_balance
        sender = Account.objects.get(number='qwe123rty098c')
        Account.confirm_transfer(10, receiver.number, sender.number)
        self.assertEqual(old_amount+10, receiver.current_balance)
