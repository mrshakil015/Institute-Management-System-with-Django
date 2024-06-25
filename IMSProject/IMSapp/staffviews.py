from django.shortcuts import render,redirect

def addstaff(request):
    return render(request,'staff/addstaff.html')


def editstaff(request):
    return render(request,'staff/editstaff.html')


def stafflist(request):
    return render(request,'staff/stafflist.html')

def viewstaff(request):
    return render(request,'staff/viewstaff.html')


