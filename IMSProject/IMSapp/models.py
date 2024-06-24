from django.db import models
from django.contrib.auth.models import AbstractUser

class IMSUserModel(AbstractUser):
    USERTYPE=[
        ('authority','Authority'),
        ('student','Student'),
        ('teacher','Teacher'),
        ('staff','Staff'),
    ]

    UserType=models.CharField(choices=USERTYPE,max_length=100, null=True)

class CourseInfoModel(models.Model):
    CourseName=models.CharField(max_length=100, null=True)
    CourseDuration=models.CharField(max_length=100, null=True)
    WeeklyClass=models.CharField(max_length=100, null=True)
    ClassDurationHour=models.CharField(max_length=100, null=True)
    ClassDurationMinute=models.CharField(max_length=100, null=True)
    CourseFee=models.CharField(max_length=100, null=True)
    AboutCourse=models.TextField(null=True)
    CourseTopics=models.CharField(max_length=100, null=True)
    CourseImage=models.ImageField(upload_to='media/courseImage', null=True)


class StudentModel(models.Model):
    Imsuser=models.OneToOneField(IMSUserModel,on_delete=models.CASCADE,related_name='studentinfo',null=True)
    StudentName=models.CharField(max_length=100,null=True)
    FatherName=models.CharField(max_length=100,null=True)
    MotherName=models.CharField(max_length=100,null=True)
    Religion=models.CharField(max_length=100,null=True)
    DOB=models.DateField(null=True)
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    Gender=models.DateField(choices=GENDER,null=True)
    Email=models.EmailField(null=True)
    Mobile=models.CharField(max_length=100,null=True)
    EmergencyContact=models.CharField(max_length=100,null=True)
    PresentAddress=models.CharField(max_length=100,null=True)
    PermanentAddress=models.CharField(max_length=100,null=True)
    StudentPhoto=models.ImageField(upload_to='media/studentPhoto',null=True)
    AdmissionDate=models.DateField(null=True)
    EducationalQualification=models.CharField(max_length=100,null=True)




class BatchInfoModel(models.Model):
    Batchuser=models.ForeignKey(StudentModel,on_delete=models.CASCADE,related_name='batchinfo',null=True)
    BatchNo=models.CharField(max_length=100,null=True)
    Batchschedule=models.CharField(max_length=100,null=True)
    Status=models.CharField(max_length=100,null=True)
    BatchStartDate=models.DateField(null=True)
    TotalStudent=models.CharField(max_length=100,null=True)
    BatchInstructor=models.CharField(max_length=100,null=True)


class TeacherModel(models.Model):
    Imsuser=models.OneToOneField(IMSUserModel,on_delete=models.CASCADE,related_name='teacherinfo',null=True)
    EmployID=models.CharField(max_length=100,null=True)
    TeacherName=models.CharField(max_length=100,null=True)
    Designation=models.CharField(max_length=100,null=True)
    FatherName=models.CharField(max_length=100,null=True)
    MotherName=models.CharField(max_length=100,null=True)
    Religion=models.CharField(max_length=100,null=True)
    DOB=models.DateField(null=True)
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    Gender=models.CharField(choices=GENDER,null=True)
    Email=models.EmailField(null=True)
    Mobile=models.CharField(max_length=100,null=True)
    EmergencyContact=models.CharField(max_length=100,null=True)
    PresentAddress=models.CharField(max_length=100,null=True)
    PermanentAddress=models.CharField(max_length=100,null=True)
    Skills=models.CharField(max_length=100,null=True)
