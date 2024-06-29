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
    
    path('teachers/',teachers,name="teachers"),
    path('courses/',courses,name="courses"),
    path('batches/',batches,name="batches"),
    path('upcommingbatch/',upcommingbatch,name="upcommingbatch"),
    path('ongoingbatch/',ongoingbatch,name="ongoingbatch"),
    path('completedbatch/',completedbatch,name="completedbatch"),
    
    #----------Contact------------
    path('contactpage/',contactpage,name="contactpage"),
    path('addcontact/',addcontact,name="addcontact"),
    path('contactlist/',contactlist,name="contactlist"),
    path('editcontact/<str:myid>',editcontact,name="editcontact"),
    path('deletecontact/<str:myid>',deletecontact,name="deletecontact"),
    
    #----------Courses------------
    
    path('categorylist/',categorylist,name="categorylist"),
    path('addcategory/',addcategory,name="addcategory"),
    path('editcategory/<str:myid>',editcategory,name="editcategory"),
    path('deletecategory/<str:myid>',deletecategory,name="deletecategory"),
    
    path('addcourse/',addcourse,name="addcourse"),
    path('courselist/',courselist,name="courselist"),
    path('editcourse/<str:myid>',editcourse,name="editcourse"),
    path('deletecourse/<str:myid>',deletecourse,name="deletecourse"),
    path('viewcourse/',viewcourse,name="viewcourse"),

    #------------Student----------------
    path('addstudent/',addstudent,name="addstudent"),
    path('editstudent/<str:myid>',editstudent,name="editstudent"),
    path('deletestudent/<str:myid>',deletestudent,name="deletestudent"),
    path('studentList/',studentlist,name="studentList"),
    path('viewstudent/',viewstudent,name="viewstudent"),
    path('studentAttendance/',studentAttendance,name="studentAttendance"),
    path('studentbatches/',studentbatches,name="studentbatches"),
    path('studentInfo/',studentInfo,name="studentInfo"),
    path('studentPayment/',studentPayment,name="studentPayment"),
    
    ##Teacher
    path('addteacher/',addteacher,name="addteacher"),
    path('editteacher/<str:teacherid>',editteacher,name="editteacher"),
    path('deleteteacher/<str:teacherid>',deleteteacher,name="deleteteacher"),
    path('teacherlist/',teacherlist,name="teacherlist"),
    path('viewteacher/',viewteacher,name="viewteacher"),
    path('teacherpersonalinfo/',teacherpersonalinfo,name="teacherpersonalinfo"),
    path('teacherbatchinfo/',teacherbatchinfo,name="teacherbatchinfo"),
    path('teachersalaryinfo/',teachersalaryinfo,name="teachersalaryinfo"),
    path('teacherattendence/',teacherattendence,name="teacherattendence"),


    #------------Batches---------------
    path('addbatch/',addbatch,name="addbatch"),
    path('batchlist/',batchlist,name="batchlist"),
    path('editbatch/<str:myid>',editbatch,name="editbatch"),
    path('deletebatch/<str:myid>',deletebatch,name="deletebatch"),
    path('viewbatch/<str:myid>',viewbatch,name="viewbatch"),

    #staff
    path('addstaff/',addstaff,name="addstaff"),
    path('editstaff/<str:myid>',editstaff,name="editstaff"),
    path('deletestaff/<str:myid>',deletestaff,name="deletestaff"),
    path('stafflist/',stafflist,name="stafflist"),
    path('viewstaff/',viewstaff,name="viewstaff"),
    
        #---------Enroll Course List----------
    path('enrollcourse/',enrollcourse,name="enrollcourse"),
    path('enrollcourselist/',enrollcourselist,name="enrollcourselist"),
    path('editenrollcourse/<str:myid>',editenrollcourse,name="editenrollcourse"),
    path('deleteenrollcourse/<str:myid>',deleteenrollcourse,name="deleteenrollcourse"),
    
    


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
