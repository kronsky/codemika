# Generated by Django 4.0.4 on 2022-04-14 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(max_length=1000, verbose_name='Text')),
                ('datecreate', models.DateTimeField(default=datetime.datetime(2022, 4, 14, 13, 45, 3, 804930))),
                ('dateupdate', models.DateTimeField(default=datetime.datetime(2022, 4, 14, 13, 45, 3, 804952))),
            ],
        ),
    ]
