# Generated by Django 3.2.7 on 2021-09-28 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20210926_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='university_logo',
            field=models.ImageField(default='default.png', upload_to='universities-logo/%Y/%m/%d/'),
        ),
    ]
