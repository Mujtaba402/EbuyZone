# Generated by Django 3.0.5 on 2020-04-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_orders_items_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
