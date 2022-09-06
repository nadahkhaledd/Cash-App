from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    number = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    current_balance = models.FloatField(default=0.0, max_length=4)

    def __str__(self):
        return self.number

    @classmethod
    def confirm_transfer(cls, amount, recievant, sender):
        amount = round(float(amount),2)
        if sender.current_balance >= amount:
            receiver_account = Account.objects.filter(number=recievant)
            if receiver_account.exists():
                if recievant != sender:
                    receiver_account = receiver_account[0]
                    sender.current_balance -= amount
                    sender.save(update_fields=['current_balance'])
                    fees = amount * 0.04
                    amount -= fees
                    receiver_account.current_balance += amount
                    receiver_account.save(update_fields=['current_balance'])
                    transaction = Transaction(amount=round(amount,2), fees=fees, type='TR', receivant=receiver_account,
                                              sender=sender)
                    transaction.save()
                    return True
        return False


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT = 'D', _('Deposit')
        WITHDRAW = 'W', _('Withdraw')
        TRANSFER = 'TR', _('Transfer')

    amount = models.FloatField(default=0.0)
    fees = models.FloatField(default=0.0)
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=2,
        choices=TransactionType.choices,
    )
    receivant = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receivant')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender')

    def save(self, *args, **kwargs):
        if self.type == 'TR':
            admin = Account.objects.get(number='admin1')
            admin.current_balance += self.fees
            admin.save(update_fields=['current_balance'])

             # Account.confirm_transfer(self.amount, self.receivant.number, self.sender.number)
        if self.type == 'D':
            self.receivant.current_balance += self.amount
            self.receivant.save(update_fields=['current_balance'])
        elif self.type == 'W':
            if self.receivant.current_balance >= self.amount:
                self.receivant.current_balance -= self.amount
                self.receivant.save(update_fields=['current_balance'])
        super(Transaction, self).save(*args, **kwargs)