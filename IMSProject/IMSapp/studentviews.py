from django.shortcuts import render,redirect, get_object_or_404
from IMSapp.forms import *
import secrets
import string
import os

#-------Random Password Generate------------
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


def addstudent(request):
    password = generate_random_password()
    if request.method == 'POST':
        studentform = StudentForm(request.POST, request.FILES)
        personalform = PersonalInfoForm(request.POST)
        
        if studentform.is_valid():
            student = studentform.save(commit = False)
            studentid = student.StudentID
            usertype= 'Student'
            
            studentuser = IMSUserModel.objects.create_user(username=studentid,password=password,UserType=usertype)
            studentuser.save()
            
            student.Imsuser=studentuser
            student.save()
            
            if personalform.is_valid():
                personalinfo = personalform.save(commit = False)
                personalinfo.Imsuser =studentuser
                personalinfo.Password =password
                personalinfo.save()
                return redirect('studentList')
    
    else:
        studentform = StudentForm()
        personalform = PersonalInfoForm()
    
    context = {
        'studentform':studentform,
        'personalform':personalform,
    }
    return render(request,'students/addstudent.html',context)

def editstudent(request, myid):
    studentdata = get_object_or_404(StudentModel, id=myid)
    personaldata = get_object_or_404(PersonalInfoModel, Imsuser=studentdata.Imsuser)
    
    img = studentdata.StudentPhoto
    if request.method == 'POST':
        studentform = StudentForm(request.POST,request.FILES, instance=studentdata)
        personalform = PersonalInfoForm(request.POST,instance=personaldata)
        
        if studentform.is_valid() and personalform.is_valid():
            student = studentform.save(commit=False)
            image = student.StudentPhoto
            if image != img:
                os.remove(img.path)
            student.save()
            personalform.save()
            return redirect('studentList') 
    else:           
        personalform = PersonalInfoForm(instance=personaldata)
        studentform = StudentForm(instance=studentdata)
    
    context = {
        'studentform': studentform,
        'personalform': personalform,
    }
    return render(request, 'students/editstudent.html', context)

def studentlist(request):
    studentdata = StudentModel.objects.all()
    personaldata = PersonalInfoModel.objects.all()
    
    combined_data = [] 
    for student in studentdata:
        personal_info = personaldata.filter(Imsuser=student.Imsuser).first()
        print("personal info1: ",student)
        print("personal info: ",personal_info)
        print(personal_info.FatherName)
        combined_data.append({
            'student': student,
            'personal_info': personal_info
        })
    context = {
        'combined_data': combined_data,
        'studentdata': studentdata
    }
    return render(request,'students/studentlist.html',context)

def deletestudent(request,myid):
    studentdata = get_object_or_404(StudentModel, id = myid)
    user = studentdata.Imsuser
    userdata = get_object_or_404(IMSUserModel,username = user)
    img = studentdata.StudentPhoto
    os.remove(img.path)
    userdata.delete()
    return redirect('studentList')

def viewstudent(request):
    return render(request,'students/viewstudent.html')





