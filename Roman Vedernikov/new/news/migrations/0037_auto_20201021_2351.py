# Generated by Django 3.1.2 on 2020-10-21 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0036_auto_20201021_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author_id',
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 23, 51, 31, 993932), verbose_name='Дата публикации'),
        ),
    ]
