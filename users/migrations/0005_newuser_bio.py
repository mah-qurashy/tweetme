# Generated by Django 3.0 on 2020-08-09 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200809_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='bio',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
