# Generated by Django 4.0.3 on 2022-03-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_listing_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='claim',
            field=models.BooleanField(default=False),
        ),
    ]