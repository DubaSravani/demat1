# Generated by Django 3.2.5 on 2021-08-12 06:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210811_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 12, 6, 38, 11, 243596, tzinfo=utc)),
        ),
    ]
