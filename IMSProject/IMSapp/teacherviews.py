from django.shortcuts import render,redirect,get_object_or_404
from IMSapp.forms import *
from IMSapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import secrets
import string
import os

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

@login_required
def addteacher(request):
    password = generate_random_password()
    if request.method == 'POST':
        teacherform = TeacherForm(request.POST,request.FILES)
        personalform = PersonalInfoForm(request.POST)
        if teacherform.is_valid():
            teacher = teacherform.save(commit = False)
            teacherid = teacher.EmployID
            usertype = 'Teacher'
            
            teacher_exists = IMSUserModel.objects.filter(username=teacherid).exists()
            if not teacher_exists:
                teacheruser = IMSUserModel.objects.create_user(username=teacherid,password=password,UserType=usertype)
                teacheruser.save()

                teacher.Imsuser=teacheruser
                teacher.save()
                if personalform.is_valid():
                    personalinfo = personalform.save(commit = False)
                    personalinfo.Imsuser = teacheruser
                    personalinfo.Password =password
                    personalinfo.save()
                    messages.success(request,'Successfully Added')
                    return redirect('teacherlist')
            else:
                messages.error(request,'User Already Exists')
    else:
        teacherform = TeacherForm()
        personalform = PersonalInfoForm()
    
    context = {
        'teacherform': teacherform,
        'personalform': personalform,
    }
    return render(request,'teachers/addteacher.html',context) 


@login_required
def editteacher(request, teacherid):
    teacherdata = get_object_or_404(TeacherModel, id=teacherid)
    personaldata = get_object_or_404(PersonalInfoModel, Imsuser=teacherdata.Imsuser)
    img = teacherdata.TeacherPhoto
    
    if request.method == 'POST':
        teacherform = TeacherForm(request.POST, request.FILES, instance=teacherdata)
        personalform = PersonalInfoForm(request.POST, instance=personaldata)
        if teacherform.is_valid() and personalform.is_valid():
            # Ensure the EmployID is not changed
            teacher = teacherform.save(commit=False)
            teacherform.instance.EmployID = teacherdata.EmployID
            
            image = teacher.TeacherPhoto
            if image != img:
                os.remove(img.path)
            teacher.save()
            personalform.save()
            messages.success(request, 'Successfully Updated')
            return redirect('teacherlist')
    else:
        teacherform = TeacherForm(instance=teacherdata)
        personalform = PersonalInfoForm(instance=personaldata)
    
    context = {
        'teacherform': teacherform,
        'personalform': personalform,
    }
    
    return render(request, 'teachers/editteacher.html', context)
 


@login_required
def teacherlist(request):
    teacherdata = TeacherModel.objects.all()
    return render(request,'teachers/teacherlist.html',{'teacherdata':teacherdata}) 


@login_required
def deleteteacher(request,teacherid):
    teacherdata=  get_object_or_404(TeacherModel,id=teacherid)
    teacherdata.delete()
    messages.success(request,'Successfully Deleted')
    return redirect('teacherlist')


@login_required
def viewteacher(request):
    return render(request,'teachers/viewteacher.html') 

@login_required
def teacherpersonalinfo(request):
    current_user=request.user
    teacherinfo=get_object_or_404(TeacherModel,Imsuser=current_user)
    context={
        'teacherinfo':teacherinfo,
    }
    return render(request,'teachers/teacherpersonalinfo.html',context) 

@login_required
def teacherbatchinfo(request):
    return render(request,'teachers/teacherbatchinfo.html') 

@login_required
def teachersalaryinfo(request):
    return render(request,'teachers/teachersalaryinfo.html') 

@login_required
def teacherattendence(request):
    return render(request,'teachers/teacherattendence.html') 