# Generated by Django 2.1.4 on 2019-03-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_auto_20190306_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='projected_life',
            field=models.DurationField(null=True),
        ),
    ]
