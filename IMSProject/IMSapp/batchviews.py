from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from IMSapp.models import *
from IMSapp.forms import *

@login_required
def addbatch(request):
    if request.method == 'POST':
        batchform = BatchInfoForm(request.POST)
        if batchform.is_valid():
            batchform.save()
            return redirect('batchlist')
    else:
        batchform = BatchInfoForm()
    context = {
        'batchform':batchform,
    }
    return render(request,"batches/addbatch.html",context)

@login_required
def batchlist(request):
    batchdata = BatchInfoModel.objects.all()
    combined_data = []
    
    for data in batchdata:
        enrolledstudent = AdmittedCourseModel.objects.filter(LearningBatch=data).count()
        print(enrolledstudent)
        combined_data.append({
            'batchdata': data, 
            'enrolledstudent': enrolledstudent,
        })
        
    context = {
        'combined_data': combined_data
    }
    return render(request, "batches/batchlist.html", context)


@login_required
def editbatch(request,myid):
    batchdata= get_object_or_404(BatchInfoModel,id=myid)
    if request.method == 'POST':
        batchform = BatchInfoForm(request.POST,instance=batchdata)
        if batchform.is_valid():
            batchform.save()
            return redirect('batchlist')
    else:
        batchform = BatchInfoForm(instance=batchdata)
    context = {
        'batchform':batchform,
    }
    return render(request,"batches/editbatch.html",context)

@login_required
def deletebatch(request,myid):
    batchdata= get_object_or_404(BatchInfoModel,id=myid)
    batchdata.delete()
    return redirect('batchlist')

@login_required
def viewbatch(request):
    return render(request,"batches/viewbatch.html")     
