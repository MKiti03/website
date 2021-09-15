# Generated by Django 3.2.7 on 2021-09-14 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_countryfact_chose_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='chose_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.country'),
        ),
        migrations.AlterField(
            model_name='universityfact',
            name='chose_university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.university'),
        ),
    ]