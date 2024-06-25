from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout

# Create your views here.
def homepage(request):
    
    
    return render(request,'common/homepage.html')

def dashboard(request):
    
    return render(request,'common/dashboard.html')

def contactpage(request):
    
    context = {
        'pagetitle':'Contact US'
    }
    return render(request,'common/contact.html',context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
    
    return render(request, 'common/login.html')