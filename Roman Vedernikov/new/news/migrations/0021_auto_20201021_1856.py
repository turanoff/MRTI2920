# Generated by Django 3.1.2 on 2020-10-21 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_auto_20201021_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 18, 56, 39, 224686), verbose_name='Дата публикации'),
        ),
    ]