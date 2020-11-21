from django.contrib import admin
from django.urls import path
from blog.views import *
urlpatterns = [
    path("",index),
    path("user/",index1),
    path('admin/', admin.site.urls),
    path("a/",indexa),
    path("and/",add1),
    path("add/",add1),
    path("q/",indexq),
    path("c/",indexc),
    path("404/",error),
]
