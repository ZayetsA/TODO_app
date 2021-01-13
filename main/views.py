from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    all_tasks = {'tasks': tasks}
    return render(request, 'main/index.html', all_tasks)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Form is not valid"

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def about(request):
    return render(request, 'main/about.html')


def delete(request, id):
    try:
        person = Task.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
