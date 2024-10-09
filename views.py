from django.shortcuts import render

from supertodo.models import ToDoItem


# Create your views here.
def home(request):
    num_tasks = ToDoItem.objects.count()
    tasks = ToDoItem.objects.all()
    return render(
        request,
        'supertodo/home.html',
        {'tasks': tasks, 'num_tasks': num_tasks},
    )


def todo_detail(request, ToDoItem_slug):
    task = ToDoItem.objects.get(slug=ToDoItem_slug)
    return render(request, 'supertodo/tasks/detail.html', {'task': task})
