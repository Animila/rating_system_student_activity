# Generated by Django 4.0.3 on 2022-03-29 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0004_placeevent_userevent_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeevent',
            name='role',
        ),
    ]