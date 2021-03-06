# Generated by Django 3.1.2 on 2020-10-24 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0043_auto_20201024_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 24, 14, 17, 26, 774432), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='Фото'),
        ),
    ]
