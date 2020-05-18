# Generated by Django 3.0.6 on 2020-05-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('subheading', models.CharField(max_length=200)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('offer_details', models.CharField(max_length=250)),
                ('t_and_c', models.CharField(blank=True, max_length=500, null=True)),
                ('offer_link', models.URLField(blank=True, max_length=250, null=True)),
                ('discount', models.CharField(blank=True, max_length=30, null=True)),
                ('coupon_code', models.CharField(blank=True, max_length=50, null=True)),
                ('normal_discount', models.CharField(blank=True, max_length=30, null=True)),
                ('price_trend', models.CharField(blank=True, max_length=50, null=True)),
                ('savings', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
