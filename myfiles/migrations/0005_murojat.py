# Generated by Django 4.1.1 on 2022-10-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0004_agents_blogs_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Murojat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('massage', models.TextField()),
                ('vaqt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
