# Generated by Django 3.1.2 on 2020-10-21 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20201021_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 23, 2, 50, 841816), verbose_name='Дата публикации'),
        ),
    ]
