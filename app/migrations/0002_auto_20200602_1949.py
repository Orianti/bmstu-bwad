# Generated by Django 3.0.6 on 2020-06-02 19:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='registration_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='service_data',
            field=models.DateField(verbose_name='дата сервиса'),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='type',
            field=models.IntegerField(choices=[(0, 'SPEED'), (1, 'AVERAGE_SPEED'), (2, 'RED LIGHT'), (3, 'DOUBLE WHITE LINE'), (4, 'BUS LANE'), (5, 'TOLLBOOTH'), (6, 'LEVEL CROSSING'), (7, 'CONGESTION CHARGE')], verbose_name='тип'),
        ),
    ]