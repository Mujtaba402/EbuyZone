# Generated by Django 3.0.5 on 2020-04-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200425_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
