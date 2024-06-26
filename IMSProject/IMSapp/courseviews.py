from django.shortcuts import render,redirect
from IMSapp.forms import *

##courses
def addcourse(request):
    
    if request.method == 'POST':
        courseform=CourseInfoForm(request.POST, request.FILES)
        
        if courseform.is_valid():
            courseform.save()
            return redirect('courselist')           
    else:
        courseform=CourseInfoForm()
    
    
    context = {
        'courseform':courseform,
    }
    
    return render(request,'courses/addcourse.html',context)


def courselist(request):
    return render(request,'courses/courselist.html')


def editcourse(request):
    return render(request,'courses/editcourse.html')


def viewcourse(request):
    return render(request,'courses/viewcourse.html')

