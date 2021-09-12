# Generated by Django 3.2.7 on 2021-09-12 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_program_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='university_in_country',
        ),
        migrations.RemoveField(
            model_name='university',
            name='university_fact',
        ),
        migrations.AddField(
            model_name='university',
            name='chose_country',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.country'),
        ),
        migrations.AddField(
            model_name='universityfact',
            name='chose_university',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.university'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.postcategory'),
        ),
        migrations.RemoveField(
            model_name='program',
            name='realted_university',
        ),
        migrations.AddField(
            model_name='program',
            name='realted_university',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.university'),
        ),
        migrations.CreateModel(
            name='ProgramFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact_name', models.CharField(blank=True, max_length=254, null=True)),
                ('fact_description', models.TextField(blank=True, max_length=254, null=True)),
                ('fact_icon', models.CharField(blank=True, max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('set_draft', models.BooleanField(default=True)),
                ('chose_program', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.program')),
            ],
            options={
                'verbose_name': 'Program fact',
                'verbose_name_plural': 'Programs Fact',
            },
        ),
        migrations.CreateModel(
            name='CountryFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact_name', models.CharField(blank=True, max_length=254, null=True)),
                ('fact_description', models.TextField(blank=True, max_length=254, null=True)),
                ('fact_icon', models.CharField(blank=True, max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('set_draft', models.BooleanField(default=True)),
                ('chose_country', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.country')),
            ],
            options={
                'verbose_name': 'Country fact',
                'verbose_name_plural': 'Countries Fact',
            },
        ),
    ]