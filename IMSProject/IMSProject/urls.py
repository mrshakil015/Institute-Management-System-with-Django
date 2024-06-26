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
from IMSapp.contactviews import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('dashboard/',dashboard,name="dashboard"),
    path('loginpage/',loginpage,name="loginpage"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    
    #----------Contact------------
    path('contactpage/',contactpage,name="contactpage"),
    path('addcontact/',addcontact,name="addcontact"),
    path('contactlist/',contactlist,name="contactlist"),
    path('editcontact/<str:myid>',editcontact,name="editcontact"),
    path('deletecontact/<str:myid>',deletecontact,name="deletecontact"),
    
    #----------Courses------------
    
    path('categorylist/',categorylist,name="categorylist"),
    path('addcategory/',addcategory,name="addcategory"),
    path('addcourse/',addcourse,name="addcourse"),
    path('courselist/',courselist,name="courselist"),
    path('editcourse/<str:myid>',editcourse,name="editcourse"),
    path('deletecourse/<str:myid>',deletecourse,name="deletecourse"),
    path('viewcourse/',viewcourse,name="viewcourse"),

    #------------Student----------------
    path('addstudent/',addstudent,name="addstudent"),
    path('editstudent/',editstudent,name="editstudent"),
    path('studentList/',studentlist,name="studentList"),
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
