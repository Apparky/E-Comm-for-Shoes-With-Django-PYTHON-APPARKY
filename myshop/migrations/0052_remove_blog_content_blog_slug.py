# Generated by Django 4.2 on 2023-04-11 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0051_blog_content_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_content',
            name='blog_slug',
        ),
    ]
