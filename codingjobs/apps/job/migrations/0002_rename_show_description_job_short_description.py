# Generated by Django 3.2 on 2021-04-19 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='show_description',
            new_name='short_description',
        ),
    ]
