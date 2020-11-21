FROM python
#requirements里面需要包含gunicorn
COPY requirements.txt . 
RUN  pip3 install -r requirements.txt
RUN sed -n '146 s/decode/encode/g' /usr/local/lib/python3.9/site-packages/django/db/backends/mysql/operations.py
#项目必须在setting.py里面打包tar zcf demo.tar.gz *
#静态文件不需要打包
ADD demo.tar.gz /
ENV port=9001
CMD gunicorn -w 4  -k gevent -b 0.0.0.0:${port} demo.wsgi:application
#docker run -dit --name django -e "port=9004" -p9004:9004 --restart always  django

