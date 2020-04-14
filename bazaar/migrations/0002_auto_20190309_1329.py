# Generated by Django 2.1.7 on 2019-03-09 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='date_available',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='saleproduct',
            name='date_available',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 9, 7, 59, 0, 364058, tzinfo=utc)),
        ),
    ]
