
from  django.shortcuts import HttpResponse
def add1(request):
        for i in ['a','b']:
              if i not in request.GET:
                 return HttpResponse('请添加参数a和b')
        a = request.GET['a']
        b = request.GET['b']
        if request.META.get('HTTP_X_FORWARDED_FOR'):
           ip= request.META.get('HTTP_X_FORWARDED_FOR')
        else:
           ip= request.META.get('REMOTE_ADDR')
        c = int(a)+int(b)
        return HttpResponse(str(c)+str(ip))
