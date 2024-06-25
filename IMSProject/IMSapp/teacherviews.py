from django.shortcuts import render,redirect

def addteacher(request):
    return render(request,'teachers/addteacher.html') 
def editteacher(request):
    return render(request,'teachers/editteacher.html') 
def teacherlist(request):
    return render(request,'teachers/teacherlist.html') 
def viewteacher(request):
    return render(request,'teachers/viewteacher.html') 