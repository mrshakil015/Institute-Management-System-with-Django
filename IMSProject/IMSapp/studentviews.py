from django.shortcuts import render,redirect
from IMSapp.forms import *


def addstudent(request):
    if request.method == 'POST':
        studentform = StudentForm(request.POST)
        personalform = PersonalInfoForm(request.POST)
        courseform = AdmittedCourseForm(request.POST)
        
        if studentform.is_valid():
            student = studentform.save(commit = False)
            studentname = student.StudentName
            studentid = student.StudentID
            password = studentname+studentid
            usertype= 'Student'
            
            studentuser = IMSUserModel.objects.create_user(username=studentid,password=password,UserType=usertype)
            studentuser.save()
            
            student.Imsuser=studentuser
            student.save()
            
            if personalform.is_valid():
                personalinfo = personalform.save(commit = False)
                personalinfo.Imsuser =studentuser
                personalinfo.save()
                
                if courseform.is_valid():
                    courseinfo = courseform.save(commit = False)
                    coursefee = courseinfo.CourseFee
                    payment = courseinfo.Payment
                    
                    courseinfo.Courseuser = studentuser
                    courseinfo.Due = int(coursefee)-int(payment)
                    courseinfo.save()
                    return redirect('studentList')
            
    
    else:
        studentform = StudentForm()
        personalform = PersonalInfoForm()
        courseform = AdmittedCourseForm()
    
    context = {
        'studentform':studentform,
        'personalform':personalform,
        'courseform':courseform,
    }
        
    return render(request,'students/addstudent.html',context)


def editstudent(request):
    return render(request,'students/editstudent.html')

def studentlist(request):
    return render(request,'students/studentlist.html')

def viewstudent(request):
    return render(request,'students/viewstudent.html')






