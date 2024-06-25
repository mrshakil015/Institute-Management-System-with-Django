from django.shortcuts import redirect, render

def addbatch(request):
    return render("batches/addbatch.html")

def batchlist(request):
    return render("batches/batchlist.html")

def editbatch(request):
    return render("batches/editbatch.html")

def viewbatch(request):
    return render("batches/viewbatch.html")
