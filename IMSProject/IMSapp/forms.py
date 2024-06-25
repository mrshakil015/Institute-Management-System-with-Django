from django import forms
from IMSapp.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseInfoModel
        fields = "__all__"
        #exclude = []

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        #exclude = []

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = "__all__"
        #exclude = []

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffModel
        fields = "__all__"
        #exclude = []

class BatchInfoForm(forms.ModelForm):
    class Meta:
        model = BatchInfoModel
        fields = "__all__"
        #exclude = []