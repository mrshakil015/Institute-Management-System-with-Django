from django.shortcuts import render

# Create your views here.
def homepage(request):
    
    
    return render(request,'homepage.html')

def contactpage(request):
    
    context = {
        'pagetitle':'Contact US'
    }
    return render(request,'contact.html',context)
