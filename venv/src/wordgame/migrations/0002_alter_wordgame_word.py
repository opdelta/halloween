# Generated by Django 4.1 on 2022-08-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordgame',
            name='word',
            field=models.CharField(max_length=100),
        ),
    ]
