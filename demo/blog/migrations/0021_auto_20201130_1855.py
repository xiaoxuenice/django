# Generated by Django 2.2.1 on 2020-11-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]