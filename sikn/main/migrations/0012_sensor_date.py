# Generated by Django 4.1.7 on 2023-02-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_sensor_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]