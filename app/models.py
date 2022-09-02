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
        sender_account = Account.objects.filter(number=sender)
        if sender_account.exists():
            sender_account = sender_account.get(number=sender)
            if sender_account.current_balance >= amount:
                receiver_account = Account.objects.filter(number=recievant)
                if receiver_account.exists():
                    if recievant != sender:
                        receiver_account = receiver_account.get(number=recievant)
                        receiver_account.current_balance += amount
                        receiver_account.save(update_fields=['current_balance'])
                        sender_account.current_balance -= amount
                        sender_account.save(update_fields=['current_balance'])
                        return True
        return False

class Transaction(models.Model):
    amount = models.FloatField(default=0.0)
    type = models.CharField(max_length=150)
    receivant = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receivant')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender')

    def save(self, *args, **kwargs):
        Account.confirm_transfer(self.amount, self.receivant.number, self.sender.number)
        super(Transaction, self).save(*args, **kwargs)