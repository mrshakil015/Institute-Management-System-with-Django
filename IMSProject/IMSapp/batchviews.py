from django.shortcuts import redirect, render

def addbatches(request):
    return render("batches/addbatches.html")

def batchlist(request):
    return render("batches/batchlist.html")

def editbatch(request):
    return render("batches/editbatch.html")

def viewbatch(request):
    return render("batches/viewbatch.html")
