from django.test import TestCase
import django.utils.timezone as timezone
import datetime
from .models import Transaction


class TransactionTest(TestCase):
    def test_was_created_recently(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_transaction = Transaction(date=time)
        self.assertNotEquals(future_transaction.date, timezone.now())
