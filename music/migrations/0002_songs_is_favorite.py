# Generated by Django 2.0.4 on 2018-04-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
