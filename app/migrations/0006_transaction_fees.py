# Generated by Django 4.0.3 on 2022-09-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='fees',
            field=models.FloatField(default=0.0),
        ),
    ]
