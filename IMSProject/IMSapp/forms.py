from django import forms
from IMSapp.models import *

class CourseInfoForm(forms.ModelForm):
    class Meta:
        model = CourseInfoModel
        fields = "__all__"
        lebels = {
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

        #exclude = []

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        labels = {
            "StudentName":"Student Name",
            "StudentPhoto":"Student Photo",
            "AdmissionDate":"Admission Date",
            "EducationalQualification":"Educational Qualification",
            "LinkedInLink":"LinkedIn Link",
            "GithubLink":"Github Link",
            "FacebookLink":"Facebook Link",
        }
        #exclude = []

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
        #exclude = []