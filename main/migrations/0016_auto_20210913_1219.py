# Generated by Django 3.2.7 on 2021-09-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210912_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='set_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]