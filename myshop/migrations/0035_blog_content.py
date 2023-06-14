# Generated by Django 3.2.18 on 2023-04-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0034_testimonials_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(default='Blog Title Here', max_length=300)),
                ('blog_summary', models.CharField(default='Blog Summary in few Words', max_length=450)),
                ('blog_heading_1', models.CharField(default='Blog Heading 1', max_length=200)),
                ('blog_intro', models.TextField(default='Blog Intro')),
                ('sub_heading_1', models.CharField(default='Sub Heading 1', max_length=500)),
                ('sub_body_1', models.TextField(default='Sub Body 1')),
                ('sub_image_1', models.FileField(blank=True, null=True, upload_to='midea/images/')),
                ('sub_image_ALT_TAG_1', models.CharField(blank=True, default='Sub Image Default ALT TAG 1', max_length=500, null=True)),
            ],
        ),
    ]
