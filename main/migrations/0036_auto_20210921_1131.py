# Generated by Django 3.2.7 on 2021-09-21 11:31

from django.db import migrations, models
import fontawesome_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_program_program_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_image',
            field=models.ImageField(default='default.png', upload_to='blog-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_flag',
            field=models.ImageField(default='default.png', upload_to='countries-flags/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_image',
            field=models.ImageField(default='default.png', upload_to='countries-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='post_category_image',
            field=models.ImageField(default='default', upload_to='blog-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_icon',
            field=fontawesome_5.fields.IconField(blank=True, default='Graduation Cap', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_image',
            field=models.ImageField(default='default.png', upload_to='programs-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='programcategory',
            name='program_category_image',
            field=models.ImageField(default='default', upload_to='programs-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='testimonials-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='university',
            name='university_image',
            field=models.ImageField(default='default.png', upload_to='universities-images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='university',
            name='university_logo',
            field=models.ImageField(default='default.png', upload_to='universities-images/%Y/%m/%d/'),
        ),
    ]
