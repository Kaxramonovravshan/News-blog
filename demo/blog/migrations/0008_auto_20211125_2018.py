# Generated by Django 3.2.6 on 2021-11-25 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211125_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 25, 15, 18, 28, 166582, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]