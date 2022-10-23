from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully Functional Ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This website represents my portfolio'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'End to end fully featured social network'
    },
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return  render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    
    return  render(request, "projects/single-project.html", {'project':projectObj })
