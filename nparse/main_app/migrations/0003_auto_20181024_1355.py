# Generated by Django 2.1.2 on 2018-10-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_company_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insider',
            name='name',
            field=models.TextField(max_length=256, unique=True, verbose_name='Name'),
        ),
    ]
