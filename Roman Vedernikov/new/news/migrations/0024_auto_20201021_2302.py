# Generated by Django 3.1.2 on 2020-10-21 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20201021_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.CharField(max_length=50, verbose_name='АВТОР'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 23, 2, 35, 962787), verbose_name='Дата публикации'),
        ),
    ]
