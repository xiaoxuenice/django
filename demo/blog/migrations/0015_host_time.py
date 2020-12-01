# Generated by Django 2.2.1 on 2020-11-28 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='time',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='time'),
            preserve_default=False,
        ),
    ]
