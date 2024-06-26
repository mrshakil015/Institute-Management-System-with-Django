from django.shortcuts import render,redirect,get_object_or_404
from IMSapp.forms import *
import os

#------------Course Category---------
def categorylist(request):
    categorydata = CourseCategoryModel.objects.all()
    
    return render(request,'courses/categorylist.html',{'categorydata':categorydata})

def addcategory(request):
    if request.method == 'POST':
        categoryform = CourseCategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('categorylist')
    else:
        categoryform = CourseCategoryForm()
    
    return render(request,'courses/addcategory.html',{'categoryform':categoryform})

#------------Admin Courses-------------
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
    coursedata = CourseInfoModel.objects.all()
    context = {
        'coursedata':coursedata
    }
    return render(request,'courses/courselist.html',context)

def editcourse(request,myid):
    coursedata = get_object_or_404(CourseInfoModel,id=myid)
    img = coursedata.CourseImage
    if request.method == 'POST':
        courseform = CourseInfoForm(request.POST, request.FILES, instance=coursedata)
        if courseform.is_valid():
            course = courseform.save(commit=False)
            image = course.CourseImage
            print("Image is: ",image)
            if image != img:
                os.remove(img.path)
            course.save()
            return redirect('courselist')
    else:
        courseform = CourseInfoForm(instance=coursedata)
    context = {
        'courseform':courseform,
    }
    return render(request,'courses/editcourse.html',context)

def deletecourse(request,myid):
    coursedata = get_object_or_404(CourseInfoModel,id=myid)
    img = coursedata.CourseImage
    os.remove(img.path)
    coursedata.delete()
    return redirect('courselist')

def viewcourse(request):
    return render(request,'courses/viewcourse.html')

