# Generated by Django 2.1.2 on 2018-10-23 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Abbreviation')),
                ('name', models.TextField(blank=True, max_length=256, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, verbose_name='Date')),
                ('open', models.FloatField(blank=True, null=True, verbose_name='Open')),
                ('high', models.FloatField(blank=True, null=True, verbose_name='High')),
                ('low', models.FloatField(blank=True, null=True, verbose_name='Low')),
                ('close', models.FloatField(blank=True, null=True, verbose_name='Close/Last')),
                ('volume', models.FloatField(blank=True, null=True, verbose_name='Volume')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Company', verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='Insider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=256, verbose_name='Name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Company', verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='InsiderRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, verbose_name='Date')),
                ('open', models.FloatField(blank=True, null=True, verbose_name='Open')),
                ('high', models.FloatField(blank=True, null=True, verbose_name='High')),
                ('low', models.FloatField(blank=True, null=True, verbose_name='Low')),
                ('close', models.FloatField(blank=True, null=True, verbose_name='Close/Last')),
                ('volume', models.FloatField(blank=True, null=True, verbose_name='Volume')),
                ('insider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Insider', verbose_name='Insider')),
            ],
        ),
    ]
