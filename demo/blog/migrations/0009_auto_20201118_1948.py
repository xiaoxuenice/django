# Generated by Django 2.2.1 on 2020-11-18 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201118_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wenzhangb',
            name='author',
        ),
        migrations.RemoveField(
            model_name='wenzhangb',
            name='tags',
        ),
        migrations.DeleteModel(
            name='biaojib',
        ),
        migrations.DeleteModel(
            name='wenzhangb',
        ),
        migrations.DeleteModel(
            name='zuozheb',
        ),
    ]