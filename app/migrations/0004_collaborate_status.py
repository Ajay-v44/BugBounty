# Generated by Django 4.2 on 2024-02-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborate',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
