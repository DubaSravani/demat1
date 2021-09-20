# Generated by Django 3.2.5 on 2021-08-03 04:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 4, 25, 18, 838055, tzinfo=utc)),
        ),
    ]
