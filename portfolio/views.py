from django.shortcuts import render
from .models import project

def show_project(request):
    projects = project.objects.all()
    return render(request,'portfolio/templates.html/',{'projects':projects})
