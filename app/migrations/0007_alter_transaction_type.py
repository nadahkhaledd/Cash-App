# Generated by Django 4.0.3 on 2022-09-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_transaction_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('D', 'Deposit'), ('W', 'Withdraw'), ('TR', 'Transfer')], max_length=2),
        ),
    ]
