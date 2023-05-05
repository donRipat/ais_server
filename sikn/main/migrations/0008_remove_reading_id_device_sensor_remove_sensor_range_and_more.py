# Generated by Django 4.1.1 on 2023-02-15 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_apparatus_options_alter_status_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='id_device_sensor',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='range',
        ),
        migrations.AddField(
            model_name='sensor',
            name='current',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='device',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.device'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='lower',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='upper',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='parameter',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Device_Sensor',
        ),
        migrations.DeleteModel(
            name='Parameter',
        ),
        migrations.DeleteModel(
            name='Range',
        ),
        migrations.DeleteModel(
            name='Reading',
        ),
        migrations.DeleteModel(
            name='SensorName',
        ),
    ]