# Generated by Django 3.2.7 on 2021-10-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interprise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.png', upload_to='testimonials-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile_pic',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
