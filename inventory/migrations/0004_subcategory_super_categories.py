# Generated by Django 4.2.2 on 2023-07-31 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_super_image_supercategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='super_categories',
            field=models.ManyToManyField(to='inventory.supercategory'),
        ),
    ]
