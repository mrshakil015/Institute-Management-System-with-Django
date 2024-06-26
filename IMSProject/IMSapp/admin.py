from django.contrib import admin
from IMSapp.models import *

class IMSUserModel_Display(admin.ModelAdmin):
    list_display=['username','UserType','email']
admin.site.register(IMSUserModel,IMSUserModel_Display)

class PersonalInfoModel_Display(admin.ModelAdmin):
    list_display=['Imsuser','Mobile']
admin.site.register(PersonalInfoModel,PersonalInfoModel_Display)


class CourseInfoModel_Dispaly(admin.ModelAdmin):
    list_display=['CourseName','CourseDuration']
admin.site.register(CourseInfoModel,CourseInfoModel_Dispaly)


class StudentModel_Dispaly(admin.ModelAdmin):
    list_display=['Imsuser','StudentName','EducationalQualification']
admin.site.register(StudentModel,StudentModel_Dispaly)


class BatchInfoModel_Dispaly(admin.ModelAdmin):
    list_display=['BatchNo','BatchInstructor']
admin.site.register(BatchInfoModel,BatchInfoModel_Dispaly)


class TeacherModel_Dispaly(admin.ModelAdmin):
    list_display=['Imsuser','TeacherName','Designation']
admin.site.register(TeacherModel,TeacherModel_Dispaly)

class StaffModel_Display(admin.ModelAdmin):
    list_display=['Imsuser','StaffName','EmployID']
admin.site.register(StaffModel,StaffModel_Display)

class AdmittedCourseModel_Display(admin.ModelAdmin):
    list_display=['Courseuser','CourseName']
admin.site.register(AdmittedCourseModel,AdmittedCourseModel_Display)

##Salary Model
class SalaryModel_Display(admin.ModelAdmin):
    list_display=['Imsuser','Salary']
admin.site.register(SalaryModel,SalaryModel_Display)

admin.site.register(WebsiteContactModel)
        

                    
                    




