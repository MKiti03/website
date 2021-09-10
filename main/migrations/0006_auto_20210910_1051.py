# Generated by Django 3.2.7 on 2021-09-10 10:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_pages'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(blank=True, max_length=254, null=True)),
                ('psot_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_image', models.ImageField(default='default.png', upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blogs Post',
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category_title', models.CharField(blank=True, max_length=254, null=True)),
                ('post_category_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pOst_category_image', models.ImageField(default='default', upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Post Category',
                'verbose_name_plural': 'POsst Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(blank=True, max_length=254, null=True)),
                ('review', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('review_star_number', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('blog_post', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='main.blogpost')),
            ],
            options={
                'verbose_name': 'POst reviews',
                'verbose_name_plural': 'Posst reviews',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='main.postcategory'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_tag',
            field=models.ManyToManyField(blank=True, to='main.Tag'),
        ),
    ]
