# Generated by Django 3.2.5 on 2021-09-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
