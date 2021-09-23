# Generated by Django 3.2.7 on 2021-09-22 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_remove_getintouch_additinal_infoemation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='emial',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='country_of_residence',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='additinal_infoemation',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='course_of_interest',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='educational_qualification',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='graduation_year',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='last_mame',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='nationality',
        ),
    ]