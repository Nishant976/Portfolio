# Generated by Django 4.2 on 2024-03-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0007_rename_files_downloadcv_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='downloadcv',
            new_name='resume',
        ),
    ]
