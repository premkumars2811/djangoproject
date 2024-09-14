from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render (request,'home-todo.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful!")
            return redirect('home')
        
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


# Create your views here.
def home(request):
    task=Task.objects.filter(is_completed=False)
    completed=Task.objects.filter(is_completed=True)
    context={
        'task':task,
        'complete':completed,
    }
    return render(request,'home-todo.html',context)
def add_task(request):
    if request.method=='POST':
        task=request.POST.get('task')
        Todo=Task.objects.create(task=task)
        Todo.save()
        return redirect('home')
def mark_as_done(request,task_id):
    task=Task.objects.get(id=task_id)
    task.is_completed=True
    task.save()
    return redirect('home')
def mark_as_undone(request,task_id):
    task=Task.objects.get(id=task_id)
    task.is_completed=False
    task.save()
    return redirect('home')
def update_task(request,update_id):
    get_task=get_object_or_404(Task,id=update_id)
    if request.method=='POST':
        new_task=request.POST.get('new_task')
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task
        }
        return render(request,'update.html',context)
    
def delete_task(request,delete_id):
    delete_task=get_object_or_404(Task,id=delete_id)
    delete_task.delete()
    return redirect('home')
    
    