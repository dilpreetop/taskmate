from django import forms
from todolist_app.models import tasklist
from django.contrib.auth.models import User


class Taskform(forms.ModelForm):
    class Meta:
      model=tasklist
      fields= ['task','done']
         
        

