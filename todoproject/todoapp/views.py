from django.shortcuts import render, redirect
from . models import Task
from . forms import Todoform

# Create your views here.
def home(request):
    task1 = Task.objects.all ()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
# def details(request):
#
#     return render(request,'detail.html',)

# Here we are going to create a function which delete the tasks with respect to the Id
def delete(request,taskid):
    # getting the task id
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        # returning to the homepage
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None, instance=task) #here we passing the id(whic is stored in the variable task to instance for updating
    if f.is_valid():
        f.save() # saving the form after the update
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})