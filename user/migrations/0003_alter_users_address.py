# Generated by Django 3.2.5 on 2021-09-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210910_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.TextField(max_length=250),
        ),
    ]
