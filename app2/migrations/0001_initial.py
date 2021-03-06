# Generated by Django 3.2.5 on 2021-08-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_mobile_number', models.BigIntegerField(unique=True)),
                ('place', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='images/%y/%m/%d')),
            ],
        ),
    ]
