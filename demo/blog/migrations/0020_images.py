# Generated by Django 2.2.1 on 2020-11-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20201129_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='img')),
            ],
        ),
    ]