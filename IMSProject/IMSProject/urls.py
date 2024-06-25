from django.contrib import admin
from django.urls import path
from IMSapp.views import *
<<<<<<< Updated upstream
from IMSapp.courseviews import *
=======
from IMSapp.studentviews import *
>>>>>>> Stashed changes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('contactpage/',contactpage,name="contactpage"),
    path('dashboard/',dashboard,name="dashboard"),
<<<<<<< Updated upstream
    
    ##courses
    
    path('addcourse/',addcourse,name="addcourse"),
    path('courselist/',courselist,name="courselist"),
    path('editcourse/',editcourse,name="editcourse"),
    path('viewcourse/',viewcourse,name="viewcourse"),
    
    
    
    
    
]
=======

    #student

    path('addstudent/',addstudent,name="addstudent"),
    path('editstudent/',editstudent,name="editstudent"),
    path('studentlist/',studentlist,name="studentlist"),
    path('viewstudent/',viewstudent,name="viewstudent"),

    ]
>>>>>>> Stashed changes
