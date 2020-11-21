from django.shortcuts import render
import time
from blog.models import *
from django.shortcuts import HttpResponse
from .forms import AddForm
def error(request):
       return  HttpResponse(str("别瞎研究，你看不懂"))
def add1(request):
        a = request.GET['a']
        b = request.GET['b']
        c = int(a)+int(b)
        return HttpResponse(str(c))
def index(request):
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
	time.sleep(1)
	return  render(request,'index.html',{'string': string,"a":a,'wz':wz})
def index1(request):
	ido = request.GET['id']
	sc=Article.objects.filter(id=ido)[0].score+1
	c=Article.objects.filter(id=ido)
	c.update(score=sc)
	a=Article.objects.get(id=ido)
	wz={"zz":a.author.name,"bt":a.title,"wza":a.content,"core":a.score,"tags":a.tags.all()[0]}
	string = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
	return  render(request,'home.html',{'string': string,'wz':wz},)
def indexa(request):
        List= ['a','b','c','','d']
        Dict={"one":'it one','two':'it two'}
        return render(request,'a.html',{'List': List,'var':100,'test': 'it test',"Dict":Dict})
def indexb(request,a,b):
     	return HttpResponse(str(int(a)+int(b)))
def indexq(request):
        return  render(request,'b.html')
def indexc(request):
        return  render(request,'c.html')
def indexd(request):
    if request.method == 'POST':# 当提交表单时
     
        form = AddForm(request.POST) # form 包含提交的数据
         
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
