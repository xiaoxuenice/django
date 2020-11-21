# Generated by Django 2.2.1 on 2020-11-18 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201118_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='biaojib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='wenzhangb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='zuozheb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qq', models.CharField(max_length=10)),
                ('addr', models.TextField(max_length=2000)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='wenzhanga',
            name='author',
        ),
        migrations.RemoveField(
            model_name='wenzhanga',
            name='tags',
        ),
        migrations.DeleteModel(
            name='biaojia',
        ),
        migrations.DeleteModel(
            name='wenzhanga',
        ),
        migrations.DeleteModel(
            name='zuozhea',
        ),
        migrations.AddField(
            model_name='wenzhangb',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.zuozheb'),
        ),
        migrations.AddField(
            model_name='wenzhangb',
            name='tags',
            field=models.ManyToManyField(to='blog.biaojib'),
        ),
    ]
