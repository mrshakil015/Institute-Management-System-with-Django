from django.contrib import admin
from django.urls import path
from IMSapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('contactpage/',contactpage,name="contactpage"),
]
