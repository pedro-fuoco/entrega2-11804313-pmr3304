# Generated by Django 4.1.1 on 2022-11-09 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='movies',
            new_name='posts',
        ),
    ]
