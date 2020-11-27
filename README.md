#默认 gunicorn 只处理动态文件，所以没加nginx访问404静态，正常

#数据库切换的时候删除app下面的migrations里面的0\*文件

#docker pull xuewenchang123/django
#补充一下日志
/usr/local/bin/gunicorn -w 4 -k gevent -b 0.0.0.0:9011 demo.wsgi:application --error-logfile /var/log/django-error.log  --access-logfile /var/log/django.log
![Image text]( https://github.com/xiaoxuenice/django/blob/master/images/a.jpg?raw=true)
![Image text]( https://github.com/xiaoxuenice/django/blob/master/images/b.jpg?raw=true)
