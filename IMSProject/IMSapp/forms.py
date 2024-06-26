from django import forms
from IMSapp.models import *

class CourseInfoForm(forms.ModelForm):
    class Meta:
        model = CourseInfoModel
        fields = "__all__"
        
        labels = {
            "CourseName":"Course Name",
            "CourseDuration":"Course Duration",
            "WeeklyClass":"Weekly Class",
            "ClassDurationHour":"Class Duration Hour",
            "ClassDurationMinute":"Class Duration Minute",
            "CourseFee":"Course Fee",
            "AboutCourse":"About Course",
            "CourseTopics":"Course Topics",
            "CourseImage":"Course Image",
        }
 
class AdmittedCourseForm(forms.ModelForm):
    class Meta:
        model = AdmittedCourseModel
        fields = "__all__"  
        exclude = ['Courseuser','CourseName','LearningBatch','AssignTeacher','AdmissionDate','Due']
        
        labels = {
            "LearningBatch":"Batch No",
            "CourseName":"Course Name",
            "CourseFee":"Course Fee",
        }    

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfoModel
        fields = "__all__"
        exclude = ['Imsuser']
        
        widgets = {
            'DOB':forms.DateInput(attrs={
                'type': 'date'
            }),
        }
        
        labels = {
            "FatherName": "Father Name",
            "MotherName": "Mother Name",
            "DOB": "Date of Birth",
            "EmergencyContact": "Emergency Contact",
            "PresentAddress": "Present Address",
            "PermanentAddress": "Permanent Address",
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        exclude = ['Imsuser','StudentPhoto','AdmissionDate','LinkedInLink','GithubLink','FacebookLink']
        
        widgets = {
            'AdmissionDate':forms.DateInput(attrs={
                'type':'date'
            }),
        }
        labels = {
            "StudentID":"Student ID No",
            "StudentName":"Student Name",
            "StudentPhoto":"Student Photo",
            "AdmissionDate":"Admission Date",
            "EducationalQualification":"Educational Qualification",
            "LinkedInLink":"LinkedIn Link",
            "GithubLink":"Github Link",
            "FacebookLink":"Facebook Link",
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = "__all__"
        labels = {
            "EmployID":"Employ ID",
            "TeacherName":"Teacher Name",
            "LinkedInLink":"LinkedIn Link",
            "GithubLink":"Github Link",
            "FacebookLink":"Facebook Link",
            "JoinDate":"Join Date",
        }
        #exclude = []

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffModel
        fields = "__all__"

        leable = {
            "StaffName":"Staff Name",
            "EmployID":"Employ ID",
            "StaffDesignation":"Staff Designation",
            "JoinDate":"Join Date",
                    }
        #exclude = []

class BatchInfoForm(forms.ModelForm):
    class Meta:
        model = BatchInfoModel
        fields = "__all__"

        leable = {
            "BatchNo":"Batch No",
            "Batchschedule":"Batchs Chedule",
            "BatchStartDate":"Batch Start Date",
            "TotalStudent":"Total Student",
            "BatchInstructor":"Batch Instructor",
        }

class WebsiteContacForm(forms.ModelForm):
    class Meta:
        model = WebsiteContactModel
        fields = "__all__"
        exclude = ['Imsuser']
    
