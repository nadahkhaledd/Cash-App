from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    number = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    current_balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.number

    @classmethod
    def confirm_transfer(cls, amount, recievant, sender):
        amount = float(amount)
        sender_account = Account.objects.get(number=sender)
        if 1 < 2:
            if sender_account.current_balance >= amount:
                receiver_account = Account.objects.get(number=recievant)
                if 1 < 2:
                    receiver_account.current_balance += amount
                    receiver_account.save(update_fields=['current_balance'])
                    sender_account.current_balance -= amount
                    sender_account.save(update_fields=['current_balance'])
                    return True
        return False
