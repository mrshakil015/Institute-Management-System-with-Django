from django.shortcuts import render,redirect

##courses
def addcourse(request):
    return render(request,'courses/addcourse.html')


def courselist(request):
    return render(request,'courses/courselist.html')


def editcourse(request):
    return render(request,'courses/editcourse.html')


def viewcourse(request):
    return render(request,'courses/viewcourse.html')

