# Generated by Django 4.2.2 on 2023-07-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_mobilebanner_subbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='leftcontainersubimages',
            name='alternate_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leftimagecontainer',
            name='alternate_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mobilebanner',
            name='alternate_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rightcontainersubimages',
            name='alternate_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rightimagecontainer',
            name='alternate_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subbanner',
            name='alternate_text',
            field=models.CharField(max_length=255, null=True),
        ),
    ]