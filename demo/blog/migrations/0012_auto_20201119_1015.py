# Generated by Django 2.2.1 on 2020-11-19 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201119_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author', verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='score',
            field=models.IntegerField(verbose_name='打分'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标记'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='author',
            name='addr',
            field=models.TextField(verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='名称'),
        ),
    ]
