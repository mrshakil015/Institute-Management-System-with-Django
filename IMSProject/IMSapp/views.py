from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from IMSapp.models import *

# Create your views here.

def homepage(request):
    coursedata = CourseInfoModel.objects.all()
    categorydata = CourseCategoryModel.objects.all()
    studentdata = StudentModel.objects.all()
    batchdata = BatchInfoModel.objects.all()
    teacherdata = TeacherModel.objects.all()
    
    coursecount = coursedata.count()
    studentcount = studentdata.count()
    teachercount = teacherdata.count()
    
    current_path = request.path
    
    context = {
        'teacherdata':teacherdata,
        'teachercount':teachercount,
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

def teachers(request):
    teacherdata = TeacherModel.objects.all()
    current_path = request.path
    context = {
        'pagetitle':'Meet with Our Makers',
        'subtitle':'Trainers',
        'teacherdata':teacherdata,
        'path':current_path,
    }
    return render(request,'common/teachers.html',context)


def courses(request):
    coursedata = CourseInfoModel.objects.all()
    current_path = request.path
    context = {
        'pagetitle':'All Courses',
        'subtitle':'Courses',
        'coursedata':coursedata,
        'path':current_path,
    }
    
    return render(request,'common/courses.html',context)

def batches(request):
    batchdata = BatchInfoModel.objects.all()
    current_path = request.path
    print(current_path)
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/batches.html',context)

def upcommingbatch(request):
    batchdata = BatchInfoModel.objects.filter(Status='Upcomming')
    current_path = request.path
    print(current_path)
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/upcommingbatch.html',context)

def ongoingbatch(request):
    batchdata = BatchInfoModel.objects.filter(Status='On-Going')
    current_path = request.path
    print(current_path)
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/ongoingbatch.html',context)

def completedbatch(request):
    batchdata = BatchInfoModel.objects.filter(Status='Completed')
    current_path = request.path
    print(current_path)
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/completedbatch.html',context)

def contactpage(request):
    current_path = request.path
    context = {
        'pagetitle':'Contact US',
        'subtitle':'Contact',
        'path':current_path,
    }
    return render(request,'contact/contact.html',context)