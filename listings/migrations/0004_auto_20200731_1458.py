# Generated by Django 3.0.8 on 2020-07-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='photo_main_2',
            new_name='photo_card_2',
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_card_1',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
