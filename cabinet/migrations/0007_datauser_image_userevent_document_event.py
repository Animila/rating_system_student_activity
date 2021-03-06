# Generated by Django 4.0.3 on 2022-03-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0006_userevent_member_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='datauser',
            name='image',
            field=models.ImageField(default=3, upload_to='user/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userevent',
            name='document_event',
            field=models.ImageField(default=5, upload_to='user/document/'),
            preserve_default=False,
        ),
    ]
