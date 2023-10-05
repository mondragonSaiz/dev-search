from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Review, Tag

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    # for i in projects:
    #     if i['id'] == pk :
    #         project= i
    return render(request, 'projects/single-project.html', {'project': project, 'tags': tags})