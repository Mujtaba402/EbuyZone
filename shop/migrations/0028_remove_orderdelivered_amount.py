# Generated by Django 3.0.5 on 2020-06-27 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_orderdelivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdelivered',
            name='amount',
        ),
    ]
