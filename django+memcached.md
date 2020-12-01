# yum -y install memcached libevent-dev<br>
# memcached -d -m 512 -l 127.0.0.1 -p 11211 -u root<br>
# pip3 install python-memcached<br>
# vim settings.py<br>
CACHES = {<br>
 'default': {<br>
  'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', #指定缓存使用的引擎<br>
  'LOCATION': '127.0.0.1:11211',         #指定Memcache缓存服务器的IP地址和端口<br>
 }<br>
}<br><br>
# 也可以这么写<br>
CACHES = {<br>
    'default': {<br>
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',<br>
        'LOCATION': [<br>
            '172.19.26.240:11211',<br>
            '172.19.26.242:11211',<br>
        ]<br>
        #我们也可以给缓存机器加权重，权重高的承担更多的请求，如下<br>
        'LOCATION': [<br>
            ('172.19.26.240:11211',5),<br>
            ('172.19.26.242:11211',1),<br>
        ]<br>
    }<br>
 }<br>
################################################<br>
# 在代码中你可以有三种方式使用Cache。<br>
# 1，在视图View中使用<br>
from django.views.decorators.cache import cache_page<br>
@cache_page(60 * 15)<br>
def my_view(request):<br>
# 2，在URLConf中使用<br>
from django.views.decorators.cache import cache_page<br>
urlpatterns = [<br>
    path('foo/<int:code>/', cache_page(60 * 15)(my_view)),<br>
]<br>
# 3，在模板中使用<br>
<html><br>
{% load cache %}    #加载缓存<br>
<body><br>
<h1>{{ ctime }}</h1><br>
{% cache 15 'aaa' %}   #设定超时时间为15秒<br>
{{ ctime }}<br>
{% endcache %}<br>
</body><br>
</html><br>
################################################<br>
# 全站使用缓存<br>
vim setttings.py<br>
MIDDLEWARE = [<br>
    'django.middleware.cache.UpdateCacheMiddleware',<br>
    'django.middleware.common.CommonMiddleware',<br>
    'django.middleware.cache.FetchFromCacheMiddleware',<br>
]<br>
CACHE__MIDDLEWARE_SECONDS=15         #设定超时时间为15秒<br>

################################################<br>
# 清除缓存<br>
telnet 127.0.0.1 11211<br>
flush_all<br>

