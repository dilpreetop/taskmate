from django.shortcuts import render, redirect
from users_app.forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method=="POST":
        register_form= CustomRegisterForm(request.POST)
        if register_form.is_valid():
         register_form.save()
         messages.success(request,("A NEW USER ACCOUNT CREATED,PLEASE LOGIN"))
         return redirect('register')
        
    else:
     register_form= CustomRegisterForm()  
    return render(request, 'register.html',{'register_form':register_form})