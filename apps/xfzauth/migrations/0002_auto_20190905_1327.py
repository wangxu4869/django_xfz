# Generated by Django 2.0 on 2019-09-05 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xfzauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='data_joinde',
            new_name='data_joined',
        ),
    ]
