from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def projects(request):
    return  HttpResponse("here are our projects")


def project(request, pk):
    return  HttpResponse("Single Project" + " " + str(pk))
