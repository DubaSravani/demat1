# Generated by Django 3.2.5 on 2021-08-03 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210803_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 15, 39, 41, 113825, tzinfo=utc)),
        ),
    ]
