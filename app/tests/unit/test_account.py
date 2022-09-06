from django.test import TestCase
from app.models import Account
from django.contrib.auth.models import User
from datetime import date


class AccountTest(TestCase):
    def test_confirm_transfer(self):
        admin = User(username='admin', password='admin1234')
        admin_account = Account(number='admin1', date_created=date.today(), user=admin)
        admin.save()
        admin_account.save()

        user = User(username='test', password='test1234')
        receiver = Account(number='qwe123rty098h', date_created=date.today(), user=user, current_balance=150.0)
        user.save()
        receiver.save()
        user2 = User(username='test1', password='test0987')
        sender = Account(number='qwe123rty098t', date_created=date.today(), user=user2, current_balance=120.0)
        user2.save()
        sender.save()
        Account.confirm_transfer(10, receiver.number, sender)
        self.assertEqual(160.0, receiver.current_balance)
