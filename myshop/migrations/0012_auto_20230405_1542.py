# Generated by Django 3.2.18 on 2023-04-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0011_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='sub_body_1',
            field=models.TextField(default='Sub Body 1'),
        ),
        migrations.AddField(
            model_name='about_us',
            name='sub_body_2',
            field=models.TextField(default='Sub Body 2'),
        ),
        migrations.AddField(
            model_name='about_us',
            name='sub_heading_1',
            field=models.CharField(default='Sub Heading 1', max_length=300),
        ),
        migrations.AddField(
            model_name='about_us',
            name='sub_heading_2',
            field=models.CharField(default='Sub Heading 2', max_length=300),
        ),
    ]
