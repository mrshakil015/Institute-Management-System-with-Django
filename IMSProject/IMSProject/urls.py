from django.contrib import admin
from django.urls import path
from IMSapp.views import *
from IMSapp.courseviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('contactpage/',contactpage,name="contactpage"),
    path('dashboard/',dashboard,name="dashboard"),
    
    ##courses
    
    path('addcourse/',addcourse,name="addcourse"),
    path('courselist/',courselist,name="courselist"),
    path('editcourse/',editcourse,name="editcourse"),
    path('viewcourse/',viewcourse,name="viewcourse"),
    
    
    
    
    
]
