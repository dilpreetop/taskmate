from django import forms
from django.contrib.auth.models import User


class Taskform(forms.ModelForm):
    class Meta:
      model=tasklist
      fields= ['task','done']
         
        

