# Generated by Django 3.0.3 on 2020-07-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
