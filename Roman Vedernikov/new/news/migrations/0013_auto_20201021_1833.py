# Generated by Django 3.1.2 on 2020-10-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20201021_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
    ]
