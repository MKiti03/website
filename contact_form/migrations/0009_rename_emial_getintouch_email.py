# Generated by Django 3.2.7 on 2021-09-29 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0008_rename_last_mame_getintouch_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getintouch',
            old_name='emial',
            new_name='email',
        ),
    ]