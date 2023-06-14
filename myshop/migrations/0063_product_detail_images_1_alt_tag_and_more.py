# Generated by Django 4.2 on 2023-04-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0062_alter_product_detail_images_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_detail',
            name='images_1_ALT_TAG',
            field=models.CharField(default='Image 1 ALT TAG', max_length=300),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='images_2_ALT_TAG',
            field=models.CharField(default='Image 2 ALT TAG', max_length=300),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='images_3_ALT_TAG',
            field=models.CharField(default='Image 3 ALT TAG', max_length=300),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='images_4_ALT_TAG',
            field=models.CharField(default='Image 4 ALT TAG', max_length=300),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='images_5_ALT_TAG',
            field=models.CharField(default='Image 5 ALT TAG', max_length=300),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='images_6_ALT_TAG',
            field=models.CharField(default='Image 6 ALT TAG', max_length=300),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_2',
            field=models.FileField(blank=True, null=True, upload_to='midea/images/'),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_3',
            field=models.FileField(blank=True, null=True, upload_to='midea/images/'),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_4',
            field=models.FileField(blank=True, null=True, upload_to='midea/images/'),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_5',
            field=models.FileField(blank=True, null=True, upload_to='midea/images/'),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='images_6',
            field=models.FileField(blank=True, null=True, upload_to='midea/images/'),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='product_slug',
            field=models.CharField(default='This-is-product-slug', max_length=500),
        ),
    ]
