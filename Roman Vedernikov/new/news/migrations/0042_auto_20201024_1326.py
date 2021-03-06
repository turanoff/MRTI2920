# Generated by Django 3.1.2 on 2020-10-24 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0041_auto_20201023_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='', upload_to='uploads', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 24, 13, 26, 41, 744798), verbose_name='Дата публикации'),
        ),
    ]
