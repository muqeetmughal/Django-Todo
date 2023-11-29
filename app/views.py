from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


# Tasks
def task(request):
    return render(request, 'task.html')



# Todo
def todo(request):
    return render(request, 'todo.html')