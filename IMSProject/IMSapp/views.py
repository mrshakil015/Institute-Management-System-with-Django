from django.shortcuts import render

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
    
    
    return render(request, 'common/login.html')