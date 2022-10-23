from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

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
    page = "Projects"
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return  render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return  render(request, "projects/single-project.html", {'project':projectObj})
