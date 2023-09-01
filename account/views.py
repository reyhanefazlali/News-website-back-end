from django.shortcuts import render , redirect
from django .contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def login_views(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            return redirect('/')
        
    forms=AuthenticationForm()
    return render(request,'account/login.html',{'forms':forms})

@login_required()
def logout_views(request):
    logout(request)
    return redirect('/account/login/')

def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            forms=UserCreationForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('/account/login/')
            
    forms=UserCreationForm()
    return render(request,'account/signup.html',{'forms':forms})

    
