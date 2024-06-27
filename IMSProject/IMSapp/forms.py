from django import forms
from IMSapp.models import *

class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategoryModel
        fields = "__all__"
        
        labels = {
            "CategoryName":"Category Name"
        }

class CourseInfoForm(forms.ModelForm):
    class Meta:
        model = CourseInfoModel
        fields = "__all__"
        
        labels = {
            "CourseName":"Course Name",
            "Lecture":"No of Lecture",
            "ShortSummary":"Short Summary",
            "CourseCategory":"Course Category",
            "CourseDuration":"Course Duration",
            "WeeklyClass":"Weekly Class",
            "ClassDuration":"Class Duration(in Minutes)",
            "TotalProject":"Total Project",
            "CourseOverview":"Course Overview",
            "CourseCurrriculum":"Course Currriculum",
            "Software":"Course Software",
            "CourseFor":"Course For",
            "JobPositions":"Job Positions",
            "CourseFee":"Course Fee",
            "IntroVideo":"Intro Video Link",
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

        labels = {
            "StaffName":"Staff Name",
            "EmployID":"Employ ID",
            "StaffDesignation":"Staff Designation",
            "JoinDate":"Join Date",

        }

class BatchInfoForm(forms.ModelForm):
    class Meta:
        model = BatchInfoModel
        fields = "__all__"

        widgets = {
            'BatchStartDate':forms.DateInput(attrs={
                'type':'date'
            }),
            'BatchNo': forms.TextInput(attrs={
                'placeholder': 'Example: 75'
            }),
            'Batchschedule': forms.TextInput(attrs={
                'placeholder': 'Example: Sat, Mon, Wed'
            }),
            'TotalStudent': forms.TextInput(attrs={
                'placeholder': 'Example: 25'
            }),
            'BatchInstructor': forms.TextInput(attrs={
                'placeholder': 'Example: 20012, 24022'
            }),
        }
        labels = {
            "BatchNo":"Batch No",
            "Batchschedule":"Batchs Schedule",
            "BatchStartDate":"Batch Start Date",
            "TotalStudent":"Total Seat",
            "BatchInstructor":"Instructor ID No",
            "CourseName":"Course Name",
        }

class WebsiteContacForm(forms.ModelForm):
    class Meta:
        model = WebsiteContactModel
        fields = "__all__"
        exclude = ['Imsuser']
    
