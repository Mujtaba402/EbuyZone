# Generated by Django 3.0.5 on 2020-04-24 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200425_0049'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderPlaced',
            new_name='OrderUpdate',
        ),
    ]
