# Generated by Django 2.1.4 on 2019-03-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0024_assets_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='status',
            field=models.CharField(choices=[('In Use', 'Use'), ('In Storage', 'Storage'), ('In Maintenance', 'Maintenance'), ('Defective', 'Defective'), ('Archived', 'Archived')], max_length=100),
        ),
    ]
