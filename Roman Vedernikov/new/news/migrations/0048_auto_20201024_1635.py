# Generated by Django 3.1.2 on 2020-10-24 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0047_auto_20201024_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 24, 16, 35, 5, 176591), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='', upload_to='./uploads', verbose_name='Фото'),
        ),
    ]
