from django.contrib import admin
from IMSapp.models import *

class IMSUserModel_Display(admin.ModelAdmin):
    list_display=['username','UserType']
admin.site.register(IMSUserModel,IMSUserModel_Display)


class CourseInfoModel_Dispaly(admin.ModelAdmin):
    list_display=['CourseName','CourseDuration']
admin.site.register(CourseInfoModel,CourseInfoModel_Dispaly)


class StudentModel_Dispaly(admin.ModelAdmin):
    list_display=['StudentName','Gender']
admin.site.register(StudentModel,StudentModel_Dispaly)


class BatchInfoModel_Dispaly(admin.ModelAdmin):
    list_display=['BatchNo','BatchInstructor']
admin.site.register(BatchInfoModel,BatchInfoModel_Dispaly)


class TeacherModel_Dispaly(admin.ModelAdmin):
    list_display=['TeacherName','Gender']
admin.site.register(TeacherModel,TeacherModel_Dispaly)




