from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request,'common/homepage.html')

@login_required
def dashboard(request):
    
    return render(request,'common/dashboard.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
    
    return render(request, 'common/login.html')

@login_required
def logoutPage(request):
    request.user
    logout(request)
    return redirect('homepage')

