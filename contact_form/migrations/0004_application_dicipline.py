# Generated by Django 3.2.7 on 2021-11-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0003_alter_application_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='dicipline',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]