# Generated by Django 3.2.7 on 2021-09-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_realted_university_program_choose_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='program_category',
            field=models.ManyToManyField(blank=True, to='main.ProgramCategory'),
        ),
    ]
