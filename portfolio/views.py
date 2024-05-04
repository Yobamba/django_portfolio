from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import TodoItem, Project


# Create your views here.
def home(request): 
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos":items})

def index(request):
    return render(request, "index.html")

def projDetails(request, project_name):
    project = Project.objects.get(name=project_name)
    return render(request, "project_details.html", {"project": project})

def get_projects(request):
    projects = Project.objects.all().values()
    return JsonResponse(list(projects), safe=False)