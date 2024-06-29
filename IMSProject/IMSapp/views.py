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
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    
    
    coursecount = coursedata.count()
    studentcount = studentdata.count()
    teachercount = teacherdata.count()
    batchcount = batchdata.count()
    
    current_path = request.path
    
    #------No of Student in a Course
    coursestudent = []
    enrolledstudent = 0
    for course in coursedata:
        nostudent = AdmittedCourseModel.objects.filter(CourseName=course).count()
        enrolledstudent += nostudent
        coursestudent.append({
            'course':course,
            'student':nostudent,
        })
    
    context = {
        'teacherdata':teacherdata,
        'teachercount':teachercount,
        'coursestudent':coursestudent,
        'coursedata':coursedata,
        'contactdata':contactdata,
        'categorydata':categorydata,
        'coursecount':coursecount,
        'batchdata':batchdata,
        'studentcount':studentcount,
        'enrolledstudent':enrolledstudent,
        'batchcount':batchcount,
        'path':current_path,
    }
    return render(request,'common/homepage.html',context)

@login_required
def dashboard(request):
    coursedata = CourseInfoModel.objects.all()
    categorydata = CourseCategoryModel.objects.all()
    studentdata = StudentModel.objects.all()
    batchdata = BatchInfoModel.objects.all()
    teacherdata = TeacherModel.objects.all()
    admittedcourse = AdmittedCourseModel.objects.all()
    
    totalenrolledstudent = admittedcourse.count()
    totalteacher = teacherdata.count()
    totalbatch = batchdata.count()
    totalcourse = coursedata.count()
    
    combined_data = []
    
    for data in batchdata:
        enrolledstudent = AdmittedCourseModel.objects.filter(LearningBatch=data).count()
        combined_data.append({
            'batchdata': data, 
            'enrolledstudent': enrolledstudent,
        })
    
    context = {
        'teacherdata':teacherdata,
        'coursedata':coursedata,
        'categorydata':categorydata,
        'studentdata':studentdata,
        'totalenrolledstudent':totalenrolledstudent,
        'totalteacher':totalteacher,
        'totalbatch':totalbatch,
        'totalcourse':totalcourse,
        'combined_data':combined_data,
    }
    
    return render(request,'common/dashboard.html',context)

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
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    current_path = request.path
    context = {
        'pagetitle':'Meet with Our Makers',
        'subtitle':'Trainers',
        'teacherdata':teacherdata,
        'contactdata':contactdata,
        'path':current_path,
    }
    return render(request,'common/teachers.html',context)


def courses(request):
    coursedata = CourseInfoModel.objects.all()
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    
    #------No of Student in a Course
    coursestudent = []
    for course in coursedata:
        nostudent = AdmittedCourseModel.objects.filter(CourseName=course).count()
        coursestudent.append({
            'course':course,
            'student':nostudent,
        })
    current_path = request.path
    context = {
        'pagetitle':'All Courses',
        'subtitle':'Courses',
        'coursedata':coursedata,
        'coursestudent':coursestudent,
        'contactdata':contactdata,
        'path':current_path,
    }
    
    return render(request,'common/courses.html',context)

def batches(request):
    batchdata = BatchInfoModel.objects.all()
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    current_path = request.path
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'headtitle': 'List of All Batches',
        'contactdata':contactdata,
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/batches.html',context)

def upcommingbatch(request):
    batchdata = BatchInfoModel.objects.filter(Status='Upcomming')
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    current_path = request.path
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'headtitle': 'List of Upcomming Batches',
        'contactdata':contactdata,
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/upcommingbatch.html',context)

def ongoingbatch(request):
    batchdata = BatchInfoModel.objects.filter(Status='On-Going')
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    current_path = request.path
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'headtitle': 'List of On-Going Batches',
        'contactdata':contactdata,
        'batchdata':batchdata,
        'path':current_path,
    }
    
    return render(request,'common/ongoingbatch.html',context)

def completedbatch(request):
    batchdata = BatchInfoModel.objects.filter(Status='Completed')
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    current_path = request.path
    context = {
        'pagetitle':'All Batches',
        'subtitle':'Batches',
        'headtitle': 'List of Completed Batches',
        'batchdata':batchdata,
        'contactdata':contactdata,
        'path':current_path,
    }
    
    return render(request,'common/completedbatch.html',context)

def contactpage(request):
    contactdata = WebsiteContactModel.objects.get(Imsuser='Authority')
    current_path = request.path
    context = {
        'pagetitle':'Contact US',
        'subtitle':'Contact',
        'contactdata':contactdata,
        'path':current_path,
    }
    return render(request,'contact/contact.html',context)