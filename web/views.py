from django.shortcuts import render , redirect
from blog.models import News
from web.forms import ContactForm


def index(request,auth=None,cat=None):
    news=News.objects.filter(Active=1)
    if auth!=None:
        news=News.objects.filter(newswriter__username=auth)
    if cat!=None:
        news=News.objects.filter(category__name=cat)
    context={'news':news}
    return render(request,'index.html',context)



def contact(request):
    if request.method=='POST':
        forms=ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
        
    forms=ContactForm()
    return render(request,'web/contact.html',{'forms':forms})

def about(request):
    
    return render(request,'web/about.html')
