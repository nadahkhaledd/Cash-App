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
        if cls.current_balance >= amount:
            receiver_account = Account.objects.get(number=recievant)
            if receiver_account.exists():
                receiver_account.current_balance += amount
                receiver_account.save(['current_credit'])
                cls.current_balance -= amount
                cls.save()







