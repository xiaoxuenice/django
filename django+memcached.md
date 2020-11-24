yum -y install memcached libevent-dev
memcached -d -m 512 -l 127.0.0.1 -p 11211 -u root
pip3 install python-memcached
vim settings.py
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', # 指定缓存使用的引擎
  'LOCATION': '127.0.0.1:11211',         # 指定Memcache缓存服务器的IP地址和端口
  'OPTIONS':{
   'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }
 }
}
#也可以这么写
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '172.19.26.240:11211',
            '172.19.26.242:11211',
        ]
        # 我们也可以给缓存机器加权重，权重高的承担更多的请求，如下
        'LOCATION': [
            ('172.19.26.240:11211',5),
            ('172.19.26.242:11211',1),
        ]
    }
 }
################################################
在代码中你可以有三种方式使用Cache。
1，在视图View中使用
from django.views.decorators.cache import cache_page
@cache_page(60 * 15)
def my_view(request):
2，在URLConf中使用
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
]
3，在模板中使用
<html>
{% load cache %}    # 加载缓存
<body>
<h1>{{ ctime }}</h1>
{% cache 15 'aaa' %}   # 设定超时时间为15秒
 <h1>{{ ctime }}</h1>
{% endcache %}
</body>
</html>
################################################
全站使用缓存
vim setttings.py
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

################################################
# 清除缓存
telnet 127.0.0.1 11211
flush_all
