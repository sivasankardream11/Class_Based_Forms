from django import forms
from app.models import *
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

class Emp_details(forms.ModelForm):
    class Meta:
        model=Employe
        fields='__all__'
