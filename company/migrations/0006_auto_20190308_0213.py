# Generated by Django 2.1.4 on 2019-03-07 18:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20190308_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]