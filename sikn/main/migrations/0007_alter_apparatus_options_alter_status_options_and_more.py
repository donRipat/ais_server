# Generated by Django 4.1.1 on 2023-02-14 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_reading_parameter_reading_time_device_sensor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apparatus',
            options={'verbose_name_plural': 'Apparatuses'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses'},
        ),
        migrations.RemoveField(
            model_name='reading',
            name='sensor',
        ),
        migrations.AddField(
            model_name='reading',
            name='id_device_sensor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.device_sensor'),
            preserve_default=False,
        ),
    ]