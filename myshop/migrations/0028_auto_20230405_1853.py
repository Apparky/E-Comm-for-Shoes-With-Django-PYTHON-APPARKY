# Generated by Django 3.2.18 on 2023-04-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0027_auto_20230405_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='out_team',
            name='Discord_profile_Link',
            field=models.CharField(blank=True, default='Discord Link Here', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='out_team',
            name='Instagram_profile_Link',
            field=models.CharField(blank=True, default='Instagram Link Here', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='out_team',
            name='RedIT_profile_Link',
            field=models.CharField(blank=True, default='RedIT Link Here', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='out_team',
            name='Youtube_Channel_Link',
            field=models.CharField(blank=True, default='YouTube Link Here', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='out_team',
            name='linkedin_profile_Link',
            field=models.CharField(blank=True, default='Linkedin Link Here', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='out_team',
            name='twitter_profile_Link',
            field=models.CharField(blank=True, default='Twitter Link Here', max_length=400, null=True),
        ),
    ]
