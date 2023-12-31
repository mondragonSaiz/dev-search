from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm
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

def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={'form': form}
    return render(request, "projects/project_form.html", context)
    
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_project.html', context)