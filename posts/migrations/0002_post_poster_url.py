# Generated by Django 4.1.1 on 2022-11-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster_url',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
    ]
