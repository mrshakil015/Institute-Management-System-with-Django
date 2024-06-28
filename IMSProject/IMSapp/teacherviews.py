from django.shortcuts import render,redirect,get_object_or_404
from IMSapp.forms import *
from IMSapp.models import *
from django.contrib.auth.decorators import login_required

@login_required
def addteacher(request):
    if request.method == 'POST':
        teacherform = TeacherForm(request.POST)
        personalform = PersonalInfoForm(request.POST)
        if teacherform.is_valid():
            teacher = teacherform.save(commit = False)
            teacherid = teacher.EmployID
            password = teacherid
            usertype = 'Teacher'

            teacheruser = IMSUserModel.objects.create_user(username=teacherid,password=password,UserType=usertype)
            teacheruser.save()

            teacher.Imsuser=teacheruser
            teacher.save()
            if personalform.is_valid():
                personalinfo = personalform.save(commit = False)
                personalinfo.Imsuser = teacheruser
                personalinfo.save()
                return redirect('teacherlist')
    else:
        teacherform = TeacherForm()
        personalform = PersonalInfoForm()
    
    context = {
        'teacherform': teacherform,
        'personalform': personalform,
    }
    return render(request,'teachers/addteacher.html',context) 


@login_required
def editteacher(request,teacherid):
    teacherdata = get_object_or_404(TeacherModel,id=teacherid)
    personaldata = get_object_or_404(PersonalInfoModel,Imsuser=teacherdata.Imsuser)
    if request.method == 'POST':
        teacherform = TeacherForm(request.POST,instance=teacherdata)
        personalform = PersonalInfoForm(request.POST,instance=personaldata)
        if teacherform.is_valid():
            teacherform.save()
            return redirect ('teacherlist')     
    else:
        teacherform = TeacherForm(instance=teacherdata)
        personalform = PersonalInfoForm(instance=personaldata)
        comtext={
            'teacherform':teacherform,
            'personalform':personalform,
            
        }
    return render(request,'teachers/editteacher.html',comtext) 


@login_required
def teacherlist(request):
    teacherdata = TeacherModel.objects.all()
    return render(request,'teachers/teacherlist.html',{'teacherdata':teacherdata}) 


@login_required
def deleteteacher(request,teacherid):
    teacherdata=  get_object_or_404(TeacherModel,id=teacherid)
    teacherdata.delete()
    return redirect('teacherlist')


@login_required
def viewteacher(request):
    return render(request,'teachers/viewteacher.html') 