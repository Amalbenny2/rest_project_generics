# Generated by Django 4.2.3 on 2023-10-07 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turfapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='Venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turfapp.venue'),
        ),
    ]
