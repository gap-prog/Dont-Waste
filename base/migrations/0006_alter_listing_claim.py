# Generated by Django 4.0.3 on 2022-03-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_listing_address_alter_listing_claim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='claim',
            field=models.CharField(default='False', max_length=5),
        ),
    ]
