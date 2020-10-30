# Generated by Django 3.1.2 on 2020-10-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0004_auto_20201025_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='truck',
        ),
        migrations.AddField(
            model_name='car',
            name='truck',
            field=models.ManyToManyField(to='trucks.Truck'),
        ),
    ]
