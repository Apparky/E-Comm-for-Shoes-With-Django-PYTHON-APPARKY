# Generated by Django 3.2.18 on 2023-04-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0019_alter_out_team_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='out_team',
            name='profile_ID',
            field=models.FileField(blank=True, upload_to='midea/images/'),
        ),
    ]