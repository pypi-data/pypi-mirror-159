# Generated by Django 3.1.13 on 2021-10-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210914_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=256, verbose_name='username'),
        ),
    ]
