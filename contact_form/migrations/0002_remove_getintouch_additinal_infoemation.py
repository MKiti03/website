# Generated by Django 3.2.7 on 2021-09-17 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getintouch',
            name='additinal_infoemation',
        ),
    ]
