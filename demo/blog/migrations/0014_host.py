# Generated by Django 2.2.1 on 2020-11-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201119_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.TextField(verbose_name='主机')),
                ('qdsj', models.TextField(verbose_name='启动时间')),
                ('cpuhs', models.TextField(verbose_name='cpu核数')),
                ('cpulv', models.TextField(verbose_name='cpu利率')),
                ('ncdx', models.TextField(verbose_name='内存大小')),
                ('nclv', models.TextField(verbose_name='内存利率')),
                ('cpdx', models.TextField(verbose_name='磁盘大小')),
                ('wkjs', models.TextField(verbose_name='网卡接收')),
                ('wkfs', models.TextField(verbose_name='网卡发送')),
                ('ljs', models.TextField(verbose_name='连接数')),
                ('jcs', models.TextField(verbose_name='进程数')),
            ],
            options={
                'verbose_name': '监控服务器',
                'verbose_name_plural': '监控服务器',
            },
        ),
    ]
