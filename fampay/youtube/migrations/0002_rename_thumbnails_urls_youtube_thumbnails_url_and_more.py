# Generated by Django 4.1.2 on 2022-12-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtube',
            old_name='thumbnails_URLs',
            new_name='thumbnails_URL',
        ),
        migrations.RemoveField(
            model_name='youtube',
            name='publishing_datetime',
        ),
        migrations.AddField(
            model_name='youtube',
            name='channelName',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]