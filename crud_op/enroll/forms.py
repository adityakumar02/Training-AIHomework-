from django import forms
from django.db import models
from django.db.models import fields
from .models import Student

class StudentForm(forms.ModelForm):


    class Meta:
        model = Student
        fields = ('fname', 'lname','roll_no', 'mobile')
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name' 
        }



    # def __init__(self, *args, **kwargs):
    #     super(StudentForm,self).__init__(*args, **kwargs)
    #     self.fields['department'].empty_label =  "Select"
    


