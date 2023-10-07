# Generated by Django 4.2.5 on 2023-10-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfapp', '0002_customers_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='date',
        ),
        migrations.AddField(
            model_name='customers',
            name='datetime',
            field=models.DateTimeField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
