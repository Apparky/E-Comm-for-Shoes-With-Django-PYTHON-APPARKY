# Generated by Django 3.2.18 on 2023-04-04 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_rename_contact_us_contact_us_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_US_Data',
            new_name='Contact_US',
        ),
    ]