# Generated by Django 3.0.6 on 2020-05-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_details',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='subheading',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]