from django.shortcuts import render,redirect


def addstudent(request):
    return render(request,'students/addstudent.html')


def editstudent(request):
    return render(request,'students/editstudent.html')

def studentlist(request):
    return render(request,'students/studentlist.html')

def viewstudent(request):
    return render(request,'students/viewstudent.html')






