# Generated by Django 3.0.3 on 2020-07-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
