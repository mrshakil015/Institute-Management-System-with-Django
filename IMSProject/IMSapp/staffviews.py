from django.shortcuts import render,redirect
from IMSapp.forms import *
from IMSapp.models import *

def addstaff(request):
    if request.method == 'POST':
        staffform = StaffForm(request.POST)
        personalform = PersonalInfoForm(request.POST)
        
        if staffform.is_valid():
            staff = staffform.save(commit=False)
            EmployID = staff.EmployID
            password = EmployID
            userrtype = 'Staff'
            
            staffuser = IMSUserModel.objects.create_user(username=EmployID,password=password,UserType=userrtype)
            staffuser.save()
            
            staff.Imsuser=staffuser
            staff.save()
            
            if personalform.is_valid():
                personalinfo = personalform.save(commit=False)
                personalinfo.Imuser = staffuser
                personalinfo.save()
                return redirect('stafflist')
            
    else:
        staffform = StaffForm()
        personalform = PersonalInfoForm()
        
    context = {
        'staffform':staffform,
        'personalform':personalform
    }
        
    return render(request,'staff/addstaff.html',context)


def editstaff(request):
    return render(request,'staff/editstaff.html')


def stafflist(request):
    return render(request,'staff/stafflist.html')

def viewstaff(request):
    return render(request,'staff/viewstaff.html')


