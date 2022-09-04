from django.contrib import admin
from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = ['number', 'user', 'date_created']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['type', 'date', 'amount', 'receivant']


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
