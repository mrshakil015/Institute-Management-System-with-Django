from django.shortcuts import render, redirect
from IMSapp.forms import *
from IMSapp.models import WebsiteContactModel

def contactpage(request):
    
    context = {
        'pagetitle':'Contact US'
    }
    return render(request,'contact/contact.html',context)

#------------Admin Contact----------
def addcontact(request):
    if request.method == 'POST':
        contactform = WebsiteContacForm(request.POST)
        if contactform.is_valid():
            contact = contactform.save(commit=False)
            contact.Imsuser = 'Authority'
            contact.save()
            return redirect('contactlist')
    else:    
        contactform = WebsiteContacForm()
    context = {
        'contactform':contactform,
     }
    return render(request,'contact/addcontact.html',context)

def contactlist(request):
    contactdata = WebsiteContactModel.objects.all()
    
    return render(request,'contact/contactlist.html',{'contactdata':contactdata})
