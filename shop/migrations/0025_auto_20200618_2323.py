# Generated by Django 3.0.5 on 2020-06-18 18:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20200425_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orders',
            name='update_desc',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.CreateModel(
            name='OrderReceived',
            fields=[
                ('received_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=200)),
                ('items_details', models.TextField(max_length=5000)),
                ('amount', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Orders')),
            ],
        ),
    ]