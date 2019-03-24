# Generated by Django 2.1.4 on 2019-03-01 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_branches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='branches',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='branch.Branch'),
        ),
    ]