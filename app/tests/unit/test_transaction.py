from django.test import TestCase
import django.utils.timezone as timezone
import datetime
from app.models import Transaction


# class TransactionTest(TestCase):
#     def test_was_created_recently(self):
#
#         time = timezone.now()
#         future_transaction = Transaction(date=time)
#         self.assertEqual(future_transaction.date, timezone.now())