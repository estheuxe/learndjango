# Generated by Django 2.2.5 on 2019-10-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0005_auto_20191004_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Tit-le hehe'),
        ),
    ]