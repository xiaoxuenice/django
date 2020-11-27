from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
import time
from blog.models import *
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .forms import AddForm
def error(request):
       return  HttpResponse(str("别瞎研究，你看不懂"))
def add1(request):
        a = request.GET['a']
        b = request.GET['b']
        c = int(a)+int(b)
        return HttpResponse(str(c))
@cache_page(60 * 2)
def index(request):
	if request.session.get("login",None):
		a=Article.objects.values("title").count()
		if a>20:
			aa=Article.objects.all().prefetch_related("author").order_by("-id")[:6]
		else:
			aa=Article.objects.all().prefetch_related("author").order_by("-id")[:a]
		wz=[]
		n=0
		for i in aa:
			wz.append({})
			wz[n]['zz']=i.author.name
			wz[n]['bt']=i.title
			wz[n]['wza']=i.content[0:45]
			wz[n]['core']=i.score
			wz[n]['id']=i.id
			try:
				wz[n]['tags']=i.tags.all()[0]
			except Exception as f:
				wz[n]['tags']='好心情'
			n+=1
		string = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
		return  render(request,'index.html',{'string': string,"a":a,'wz':wz,'name':request.session['name']})
	else:
		return HttpResponseRedirect("/login/")

@cache_page(60 * 2)
def index1(request):
	if request.session.get("login",None):
		ido = request.GET['id']
		sc=Article.objects.filter(id=ido)[0].score+1
		c=Article.objects.filter(id=ido)
		c.update(score=sc)
		a=Article.objects.get(id=ido)
		wz={"zz":a.author.name,"bt":a.title,"wza":a.content,"core":a.score,"tags":a.tags.all()[0]}
		string = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
		return  render(request,'home.html',{'string': string,'wz':wz,'name':request.session['name']})
	else:
		return HttpResponseRedirect("/login/")
def indexa(request):
        List= ['a','b','c','','d']
        Dict={"one":'it one','two':'it two'}
        return render(request,'a.html',{'List': List,'var':100,'test': 'it test',"Dict":Dict})

@csrf_exempt
def login(request):
	if request.method == 'POST':
		try:
			m= Author.objects.get(email=request.POST['username'])
			if str(m.qq) == str(request.POST['password']):
				request.session['name']=m.name
				request.session['login']=True
				return HttpResponseRedirect("/")
			else:
				return HttpResponseRedirect("/login/")
		except  Exception as f:
				return HttpResponseRedirect("/login/")
	return render(request,'login.html')
def logout(request):
	cache._cache.flush_all()
	request.session.flush()
	return HttpResponseRedirect("/login/")
