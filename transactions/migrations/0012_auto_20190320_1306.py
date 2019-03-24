# Generated by Django 2.1.4 on 2019-03-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_transactions_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[('1', 'On Going'), ('2', 'Finished')], max_length=3),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='ttype',
            field=models.CharField(choices=[('1', 'Maintenance'), ('2', 'Transfer'), ('3', 'Dispose'), ('4', 'Recover'), ('5', 'Defective')], max_length=3),
        ),
    ]