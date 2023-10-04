from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Review, Tag
projectList = [
    {
        'id': '1',
        'title': "RoomieHunt",
        'description': 'Web app to find your best match to live with!'
    },
      {
        'id': '2',
        'title': "GoalHub",
        'description': 'All your teamwork activities, progress and more in once place!'
    },
      {
        'id': '3',
        'title': "Fridge2Table",
        'description': 'Grab your availble groceries and start creating awesome recipes!'
    },
]
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