from django.shortcuts import render,redirect,get_object_or_404
from IMSapp.forms import *
from IMSapp.models import *
from django.contrib.auth.decorators import login_required

@login_required
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
                personalinfo.Imsuser = staffuser
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

@login_required
def editstaff(request, myid):
    staffdata = get_object_or_404(StaffModel, id=myid)
    personaldata = get_object_or_404(PersonalInfoModel, Imsuser=staffdata.Imsuser)
    
    if request.method == 'POST':
        staffform = StaffForm(request.POST, instance=staffdata)
        personalform = PersonalInfoForm(request.POST, instance=personaldata)
        
        if staffform.is_valid() and personalform.is_valid():
            staffform.save()
            personalform.save()
            return redirect('stafflist')
    else:
        staffform = StaffForm(instance=staffdata)
        personalform = PersonalInfoForm(instance=personaldata)
        
    context={
        'staffform':staffform,
        'personalform':personalform,      
    }

    return render(request,'staff/editstaff.html',context)

@login_required
def deletestaff(request,myid):
    staffdata = get_object_or_404(StaffModel, id=myid)
    staffdata.delete()
    return redirect('stafflist')

@login_required
def stafflist(request):
    staffdata = StaffModel.objects.all()
    staffdata={
        'staffdata':staffdata
    }
    
    return render(request,'staff/stafflist.html',staffdata)
@login_required
def viewstaff(request):
    return render(request,'staff/viewstaff.html')


