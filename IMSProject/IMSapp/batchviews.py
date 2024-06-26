from django.shortcuts import redirect, render

def addbatch(request):
    return render(request,"batches/addbatch.html")

def batchlist(request):
    return render(request,"batches/batchlist.html")

def editbatch(request):
    return render(request,"batches/editbatch.html")

def viewbatch(request):
    return render(request,"batches/viewbatch.html")     
