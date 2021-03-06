# Generated by Django 4.0 on 2021-12-17 20:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default=datetime.datetime(2021, 12, 17, 20, 51, 41, 877385, tzinfo=utc))),
                ('Category', models.ForeignKey(default='generall', on_delete=django.db.models.deletion.CASCADE, to='task.category')),
            ],
        ),
    ]
