# Generated by Django 3.2.7 on 2021-09-16 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20210916_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='commment',
            new_name='comment',
        ),
    ]
