# Generated by Django 3.0.5 on 2020-04-24 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200424_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]