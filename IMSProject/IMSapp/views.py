from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from IMSapp.models import *
from django.urls import resolve

# Create your views here.

def homepage(request):
    coursedata = CourseInfoModel.objects.all()
    categorydata = CourseCategoryModel.objects.all()
    studentdata = StudentModel.objects.all()
    batchdata = BatchInfoModel.objects.all()
    
    coursecount = coursedata.count()
    studentcount = studentdata.count()
    
    current_path = request.path
    
    context = {
        'coursedata':coursedata,
        'categorydata':categorydata,
        'coursecount':coursecount,
        'batchdata':batchdata,
        'studentcount':studentcount,
        'path':current_path,
    }
    return render(request,'common/homepage.html',context)

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


def courses(request):
    coursedata = CourseInfoModel.objects.all()
    context = {
        'pagetitle':'All Courses',
        'subtitle':'Courses',
        'coursedata':coursedata,
    }
    
    return render(request,'common/courses.html',context)

def batches(request):
    batchdata = BatchInfoModel.objects.all()
    current_path = request.path
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/batches.html',context)


def contactpage(request):
    current_path = request.path
    context = {
        'pagetitle':'Contact US',
        'subtitle':'Contact',
        'path':current_path,
    }
    return render(request,'contact/contact.html',context)