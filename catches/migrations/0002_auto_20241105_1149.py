# Generated by Django 3.2.25 on 2024-11-05 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catchentry',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='catchentry',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='catchentry',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]