# Generated by Django 4.2 on 2023-04-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0050_alter_blog_content_blog_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='blog_slug',
            field=models.SlugField(default='Slug-Field'),
        ),
    ]
