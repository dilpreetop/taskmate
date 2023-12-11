from django.shortcuts import render,redirect

from django.http import HttpResponse
from todolist_app.models import tasklist 
from todolist_app.forms import Taskform 
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required #IT IS A DECORATER
def todolist(request):
    if request.method=="POST":
        form=Taskform(request.POST or None)
        if form.is_valid:
           instance =form.save(commit=False)
           instance.manage= request.user
           instance.save()   
           messages.success(request,("A NEW TASK HAS ADDED"))
        return redirect('todolist')
        

    
    else:
     all_tasks= tasklist.objects.filter(manage=request.user)
     paginator = Paginator(all_tasks, 6)
     page = request.GET.get('pg')
     all_tasks = paginator.get_page(page)
     

    return render(request,'todolist.html',{'all_tasks':all_tasks})
#                 (request,'htmlpage',content*it will be always in form of dictionary)


def contact(request):
    content = {
    'contact_text':"Hi welcome to contact page",
           
           
           }
    return render(request,'contact.html',content)
 
def about(request):
    content = {
    'about_text':"Hi welcome to about page",
           
           
           }
    return render(request,'about.html',content)
@login_required 
def delete_task(request, task_id):
    task= tasklist.objects.get(pk=task_id)
    if task.manage== request.user:
     task.delete()
    else:
      messages.error(request,("NO ACCESS"))  
    
      
    
    return redirect('todolist')


@login_required 
def edit_task(request, task_id):
    if request.method=="POST":
           task= tasklist.objects.get(pk=task_id)
        
           form=Taskform(request.POST or None, instance=task)
           if form.is_valid():
            form.save()
           messages.success(request,("TASK EDITED"))
           return redirect('todolist')
        

    
    else:
      task_obj= tasklist.objects.get(pk=task_id)
      return render(request,'edit.html',{'task_obj':task_obj})
  
  
@login_required 
def complete_task(request , task_id,):
    task= tasklist.objects.get(pk=task_id)
    if task.manage== request.user:
     task.done= True
     task.save()
    else:   
     messages.error(request,("NO ACCESS"))
    return redirect('todolist')


@login_required    
def pending_task(request , task_id):
    task= tasklist.objects.get(pk=task_id)
    task.done= False
    task.save()
    
    return redirect('todolist')

def index(request):
    content = {
    'index_text':"Hi welcome to Index page",
           
           
           }
    return render(request,'index.html',content)
    