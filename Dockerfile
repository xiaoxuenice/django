FROM python
#requirements里面需要包含gunicorn
#pip3 freeze > requirements.txt (复制环境)
#sed -i 's/python/python2/g' demo/settings.py (新项目更换数据库)
#rm -rf blog/migrations/0*		      (删除缓存 __pycache__一起)
#docker restart django			      (重启django)
#python3 manage.py makemigrations	
#python3 manage.py migrate			#生成迁移文件   #应用到数据库(两个一起执行)
#python3 manage.py createsuperuser	#创建管理员	
#docker 如果不需要memcache 在配置文件中禁用
COPY requirements.txt . 
RUN  pip3 install -r requirements.txt
RUN sed -i '146 s/decode/encode/g' /usr/local/lib/python3.9/site-packages/django/db/backends/mysql/operations.py
#项目必须在setting.py里面打包tar zcf demo.tar.gz *
#静态文件不需要打包
ADD demo.tar.gz /
ENV port=9001
CMD gunicorn -w 4  -k gevent -b 0.0.0.0:${port} demo.wsgi:application   --error-logfile /var/log/django-error.log  --access-logfile /var/log/django.log
#docker run -dit --name django -e "port=9004" -p9004:9004 --restart always  django

