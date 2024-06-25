from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from IMSapp.views import *
from IMSapp.courseviews import *
from IMSapp.studentviews import *
from IMSapp.batchviews import *
from IMSapp.teacherviews import *
from IMSapp.staffviews import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('contactpage/',contactpage,name="contactpage"),
    path('dashboard/',dashboard,name="dashboard"),
    path('loginpage/',loginpage,name="loginpage"),
    
    ##courses
    
    path('addcourse/',addcourse,name="addcourse"),
    path('courselist/',courselist,name="courselist"),
    path('editcourse/',editcourse,name="editcourse"),
    path('viewcourse/',viewcourse,name="viewcourse"),

    #student

    path('addstudent/',addstudent,name="addstudent"),
    path('editstudent/',editstudent,name="editstudent"),
    path('studentlist/',studentlist,name="studentlist"),
    path('viewstudent/',viewstudent,name="viewstudent"),
    
    ##Teacher
    path('addteacher/',addteacher,name="addteacher"),
    path('editteacher/',editteacher,name="editteacher"),
    path('teacherlist/',teacherlist,name="teacherlist"),
    path('viewteacher/',viewteacher,name="viewteacher"),

    #batches
    path('addbatch/',addbatch,name="addbatch"),
    path('batchlist/',batchlist,name="batchlist"),
    path('editbatch/',editbatch,name="editbatch"),
    path('viewbatch/',viewbatch,name="viewbatch"),

    #staff
    path('addstaff/',addstaff,name="addstaff"),
    path('editstaff/',editstaff,name="editstaff"),
    path('stafflist/',stafflist,name="stafflist"),
    path('viewstaff/',viewstaff,name="viewstaff"),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
