# Generated by Django 4.1.1 on 2022-09-30 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='nami',
            new_name='nomi',
        ),
    ]
