# Generated by Django 4.1.1 on 2023-01-31 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensors',
            name='id_allowed',
        ),
        migrations.AddField(
            model_name='allowedvalues',
            name='id_sensor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.sensors'),
            preserve_default=False,
        ),
    ]