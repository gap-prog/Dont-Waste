# Generated by Django 4.0.3 on 2022-03-27 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_listing_item_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]