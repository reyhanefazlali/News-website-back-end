from django.shortcuts import render
from .models import News ,Comment

def index(request,auth=None,cat=None,tag=None):
    news=News.objects.filter(Active=1)
    if auth!=None:
        news=News.objects.filter(newswriter__username=auth)
    if cat!=None:
        news=News.objects.filter(category__name=cat)
    if tag!=None:
        news=News.filter(tag__slug=tag)
    context={'news':news}
    return render(request,'index.html',context)

def sidebar_blog(request):
    return render(request,'blog/blog.html')

def blog_details(request,num):
        new=News.objects.get(pk=num)
        comments=Comment.objects.filter(Active=1,new=new)
        context={'new':new , 'comments':comments}
        return render(request,'blog/blog_details.html',context)
        
def elements(request):
    return render(request,'blog/elements.html')

def lastest_news(request):
    return render(request,'blog/lastest_news.html')

def search_news(request):
    if request.method=='GET':
        search=request.GET.get('s')
        news=News.objects.filter(content__contains=search)
    
    context={'news':news}   
    return render(request,'index.html',context)
    
    context={'news':news}
    return render(request,'blog/blog_details.html',context)