from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from IMSapp.forms import *
import secrets
import string
import os

#-------Random Password Generate------------
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


@login_required
def addstudent(request):
    password = generate_random_password()
    if request.method == 'POST':
        studentform = StudentForm(request.POST, request.FILES)
        personalform = PersonalInfoForm(request.POST)
        
        if studentform.is_valid():
            student = studentform.save(commit = False)
            studentid = student.StudentID
            usertype= 'Student'
            
            student_exists = IMSUserModel.objects.filter(username=studentid).exists()
            
            if not student_exists:
                studentuser = IMSUserModel.objects.create_user(username=studentid,password=password,UserType=usertype)
                studentuser.save()
                
                student.Imsuser=studentuser
                student.save()
                
                if personalform.is_valid():
                    personalinfo = personalform.save(commit = False)
                    personalinfo.Imsuser =studentuser
                    personalinfo.Password =password
                    personalinfo.save()
                    messages.success(request,'Successfully Added')
                    return redirect('studentList')
            else:
                messages.error(request,'User Already Exists')
    
    else:
        studentform = StudentForm()
        personalform = PersonalInfoForm()
    
    context = {
        'studentform':studentform,
        'personalform':personalform,
    }
    return render(request,'students/addstudent.html',context)

@login_required
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

@login_required
def studentlist(request):
    studentdata = StudentModel.objects.all()
    personaldata = PersonalInfoModel.objects.all()
    
    combined_data = [] 
    for student in studentdata:
        personal_info = personaldata.filter(Imsuser=student.Imsuser).first()
        combined_data.append({
            'student': student,
            'personal_info': personal_info
        })
    context = {
        'combined_data': combined_data,
        'studentdata': studentdata
    }
    return render(request,'students/studentlist.html',context)

@login_required
def deletestudent(request,myid):
    studentdata = get_object_or_404(StudentModel, id = myid)
    user = studentdata.Imsuser
    userdata = get_object_or_404(IMSUserModel,username = user)
    img = studentdata.StudentPhoto
    os.remove(img.path)
    userdata.delete()
    return redirect('studentList')

@login_required
def viewstudent(request):
    return render(request,'students/viewstudent.html')

#------------Enroll Course------------------
@login_required
def enrollcourse(request):
    if request.method == 'POST':
        courseenrollform = EnrollCourseForm(request.POST)
        if courseenrollform.is_valid():
            courseenroll = courseenrollform.save(commit=False)
            studentid = courseenroll.StudentID
            
            # Check if the student exists
            student_exists = IMSUserModel.objects.filter(username=studentid).exists()
            if student_exists:
                student = get_object_or_404(IMSUserModel, username=studentid)
                batchno = courseenroll.LearningBatch
                
                # Check if the student is already enrolled in the batch
                batch_exists = AdmittedCourseModel.objects.filter(Courseuser=student, LearningBatch=batchno).exists()
                if not batch_exists:
                    batchdata = get_object_or_404(BatchInfoModel, BatchNo=batchno)
                    courseenroll.CourseName = batchdata.CourseName
                    courseenroll.Courseuser = student
                    coursefee = courseenroll.CourseFee
                    pay = courseenroll.Payment
                    courseenroll.Due = int(coursefee) - int(pay)
                    courseenroll.save()
                    return redirect('enrollcourselist')
                else:
                    messages.warning(request,'Student already enrolled in this batch.')
            else:
                messages.warning(request,'Student does not exist.')
    else:
        courseenrollform = EnrollCourseForm()
    
    return render(request, 'students/enrollcourse.html', {'courseenrollform': courseenrollform})

@login_required
def enrollcourselist(request):
    coursedata = AdmittedCourseModel.objects.all()
    
    return render(request,'students/enrollcourselist.html',{'coursedata':coursedata})

@login_required
def editenrollcourse(request, myid):
    coursedata = get_object_or_404(AdmittedCourseModel,id=myid)
    batch= coursedata.LearningBatch
    if request.method == 'POST':
        courseenrollform = EnrollCourseForm(request.POST, instance=coursedata)
        if courseenrollform.is_valid():
            courseenroll = courseenrollform.save(commit=False)
            studentid = courseenroll.StudentID
            
            # Check if the student exists
            student_exists = IMSUserModel.objects.filter(username=studentid).exists()
            if student_exists:
                student = get_object_or_404(IMSUserModel, username=studentid)
                batchno = courseenroll.LearningBatch
                
                # Check if the student is already enrolled in the batch
                if batchno != batch:
                    batch_exists = AdmittedCourseModel.objects.filter(Courseuser=student, LearningBatch=batchno).exists()
                    if not batch_exists:
                        batchdata = get_object_or_404(BatchInfoModel, BatchNo=batchno)
                        courseenroll.CourseName = batchdata.CourseName
                        courseenroll.Courseuser = student
                        coursefee = courseenroll.CourseFee
                        pay = courseenroll.Payment
                        courseenroll.Due = int(coursefee) - int(pay)
                        courseenroll.save()
                        messages.success(request,'Successfully Updated.')
                        return redirect('enrollcourselist')
                    else:
                        messages.warning(request,'Student already enrolled in this batch.')
                        
                else:
                    courseenroll.Courseuser = student
                    coursefee = courseenroll.CourseFee
                    pay = courseenroll.Payment
                    courseenroll.Due = int(coursefee) - int(pay)
                    courseenroll.save()
                    messages.success(request,'Successfully Updated.')
                    
                    return redirect('enrollcourselist')
            else:
                messages.warning(request,'Student does not exist.')
    else:
        courseenrollform = EnrollCourseForm(instance=coursedata)
        
    return render(request, 'students/enrollcourse.html', {'courseenrollform': courseenrollform})

@login_required
def deleteenrollcourse(request,myid):
    coursedata = get_object_or_404(AdmittedCourseModel,id=myid)
    coursedata.delete()
    messages.success(request,'Enrolled Student Deleted')
    
    return redirect('enrollcourselist')
