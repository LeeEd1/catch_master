# Generated by Django 3.2.25 on 2024-11-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0002_auto_20241105_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catchentry',
            name='description',
            field=models.TextField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='catchentry',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]