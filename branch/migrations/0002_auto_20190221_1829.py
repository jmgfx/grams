# Generated by Django 2.1.4 on 2019-02-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
