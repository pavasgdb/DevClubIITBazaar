# Generated by Django 2.1.7 on 2019-03-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0003_auto_20190309_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleproduct',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
