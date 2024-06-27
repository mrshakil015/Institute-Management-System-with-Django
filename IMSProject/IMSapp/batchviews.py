from django.shortcuts import redirect, render
from IMSapp.models import *
from IMSapp.forms import *

def addbatch(request):
    batchform = BatchInfoForm()
    
    context = {
        'batchform':batchform,
    }
    return render(request,"batches/addbatch.html",context)

def batchlist(request):
    return render(request,"batches/batchlist.html")

def editbatch(request):
    return render(request,"batches/editbatch.html")

def viewbatch(request):
    return render(request,"batches/viewbatch.html")     
