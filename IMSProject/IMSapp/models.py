from django.db import models
from django.contrib.auth.models import AbstractUser

class IMSUserModel(AbstractUser):
    USERTYPE=[
        ('Authority','Authority'),
        ('Student','Student'),
        ('Teacher','Teacher'),
        ('Staff','Staff'),
    ]

    UserType=models.CharField(choices=USERTYPE,max_length=100, null=True)

class PersonalInfoModel(models.Model):
    Imsuser=models.OneToOneField(IMSUserModel,on_delete=models.CASCADE,related_name='personalinfo',null=True)
    FatherName=models.CharField(max_length=100,null=True)
    MotherName=models.CharField(max_length=100,null=True)
    Religion=models.CharField(max_length=100,null=True)
    DOB=models.DateField(null=True)
    GENDER=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    Gender=models.CharField(choices=GENDER,max_length=100,null=True)
    Mobile=models.CharField(max_length=100,null=True)
    EmergencyContact=models.CharField(max_length=100,null=True)
    PresentAddress=models.CharField(max_length=100,null=True)
    PermanentAddress=models.CharField(max_length=100,null=True)

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
    StudentPhoto=models.ImageField(upload_to='media/studentPhoto',null=True)
    AdmissionDate=models.DateField(null=True)
    EducationalQualification=models.CharField(max_length=100,null=True)
    LinkedInLink =models.CharField(max_length=150,null=True)
    GithubLink =models.CharField(max_length=150,null=True)
    FacebookLink =models.CharField(max_length=150,null=True)
    
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
    Skills=models.CharField(max_length=100,null=True)
    LinkedInLink =models.CharField(max_length=150,null=True)
    GithubLink =models.CharField(max_length=150,null=True)
    FacebookLink =models.CharField(max_length=150,null=True)
    JoinDate = models.DateField(auto_now_add=True,null=True)
    
class ContactModel(models.Model):
    Mobile = models.CharField(max_length=50,null=True)
    Address = models.CharField(max_length=100,null=True)
    Email = models.CharField(max_length=100,null=True)
    MapLink = models.TextField(null=True)
    GithubLink =models.CharField(max_length=150,null=True)
    FacebookLink =models.CharField(max_length=150,null=True)
    YoutubeLink =models.CharField(max_length=150,null=True)
    TwitterLink =models.CharField(max_length=150,null=True)
    
    def __str__(self):
        return self.Mobile

## AdmittedCourseModel

class AdmittedCourseModel:
    Courseuser=models.OneToOneField(StudentModel,on_delete=models.CASCADE,null=True)
    AssignTeacher=models.ForeignKey(TeacherModel,on_delete=models.CASCADE,null=True)
    LearningBatch=models.OneToOneField(BatchInfoModel,on_delete=models.CASCADE,null=True)
    CourseName=models.ForeignKey(CourseInfoModel,on_delete=models.CASCADE,null=True)
    CourseFee=models.CharField(max_length=150,null=True)
    Payment=models.CharField(max_length=150,null=True)
    Due=models.CharField(max_length=150,null=True)
    AdmissionDate=models.DateField(null=True) 


## StaffModel
class StaffModel(models.Model):
    Imsuser=models.OneToOneField(IMSUserModel, on_delete=models.CASCADE,null=True)
    StaffName=models.CharField(max_length=150,null=True)
    EmployID=models.CharField(max_length=150,null=True)
    StaffDesignation=models.CharField(max_length=150,null=True)
    JoinDate = models.DateField(auto_now_add=True,null=True)

## ‍SalaryModel

class SalaryModel(models.Model):
    Imsuser=models.ForeignKey(IMSUserModel, on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=150,null=True)
    Salary=models.CharField(max_length=150,null=True)
    PaymentDate=models.DateField(null=True)