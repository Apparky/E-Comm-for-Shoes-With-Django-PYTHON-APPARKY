# Generated by Django 4.2 on 2023-04-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0052_remove_blog_content_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='blog_slug',
            field=models.SlugField(default='Blog-Slug-Field'),
        ),
    ]
