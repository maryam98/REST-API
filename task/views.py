from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from task.models import Category,TodoTask
from task.forms import TaskCreatedForm
from django.views.generic import DetailView



# Create your views here.

def show_task (request):
    query=TodoTask.objects.all().order_by('created')
    form=TaskCreatedForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
    else:
       
        form = TaskCreatedForm()
    dic={
        'query':query,
        'form':form}
    

    return render(request,'task/index.html',dic)


class TaskDetail(DetailView):
    model = TodoTask
    template_name = "task/detail.html"


def delete_task(request,id):
    task=get_object_or_404(TodoTask,id=id)
    task.delete()
    return redirect('show_task')