# Generated by Django 3.2.25 on 2024-11-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0003_auto_20241105_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catchentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
